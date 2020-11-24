#%%
import sqlite3
import pandas as pd
import os 
import gen_csv_functions as gen_csv
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in tables
deployment = pd.read_sql_query('SELECT * from deployment', connection)
instSerial = pd.read_sql_query('SELECT * from instSerial', connection)
instrument = pd.read_sql_query('SELECT * from instrument', connection)
outDef = pd.read_sql_query('SELECT * from outDef', connection)
position = pd.read_sql_query('SELECT * from position', connection)
site = pd.read_sql_query('SELECT * from site', connection)

#close connection
connection.close()
#%%
# get list of all sites 
sites_to_process = site['id']
# create csvs for every site
for process_site in sites_to_process:
    #get the network
    network = site.loc[site['id'] == process_site, 'network'].values[0]
    #init dirs
    network_dir = os.path.join("..", "source", 'networks', network, "sites")
    if os.path.exists(network_dir) == False:
        os.makedirs(network_dir)

    ## get the site meta ## 
    process_site_info = site.loc[site['id'] == process_site].T
    #renane cols, get units 
    process_site_cols = {'id' : 'Site ID', 'fullName' : 'Full Name', 'network' : 'Network',
                        'longitude' : 'Longitude', 'latitude' : 'Latitude', 'startDate' : 'Start date', 
                        'endDate' : 'End date', 'displacementHeight' : 'Displacement height', 'city' : 'City'}
    process_site_units = ['NA', 'NA', 'NA', 'degrees', 'degrees', 'UTC', 'UTC', 'm', 'NA']
    process_site_info = gen_csv.wrangle_cols(process_site_info, process_site_cols, process_site_units, col_ind = 'ind')

    #save the site meta
    meta_out_name = f"{process_site}_meta.csv"
    meta_out_dir = os.path.join(network_dir, "meta")
    gen_csv.save_to_csv(process_site_info, meta_out_dir, meta_out_name, header = False, index = True)

    ## get deployment info at site ##
    site_deployments = deployment[deployment['siteId'] == process_site]
    site_deployments_pos = site_deployments.merge(position, left_on = 'id', right_on = 'deploymentId')
    site_deployments_pos_ser = site_deployments_pos.merge(instSerial, left_on = 'instSerial', right_on = 'serial')

    # format dates to only include time
    site_deployments_pos_ser['startDate'] = site_deployments_pos_ser['startDate'].apply(lambda x: x.split(' ')[0])
    site_deployments_pos_ser['endDate'] = site_deployments_pos_ser['endDate'].apply(lambda x: x.split(' ')[0] if x != None else x)
    #rename deployment now 
    site_deployments_pos_ser = site_deployments_pos_ser.rename(columns = {'deploymentId' : 'Deployment ID'})
    #get a copy here
    site_deployments_pos_ser2 = site_deployments_pos_ser.copy()
    # format instID and serials to references 
    site_deployments_pos_ser['instId'] = site_deployments_pos_ser['instId'].apply(lambda x: f":ref:`{x}`")
    site_deployments_pos_ser['instSerial'] = site_deployments_pos_ser['instSerial'].apply(lambda x: f":ref:`{x}`")
    #remove SWTWXSTATION id from SWT table (this is required for processing but not very accurate)
    if process_site == 'SWT':
        site_deployments_pos_ser = site_deployments_pos_ser.loc[site_deployments_pos_ser['instId'] != 'SWTWXSTATION']


    # filter columns for date of deployments 
    dates_cols = {'Deployment ID' : 'Deployment ID', 'instId' : 'Instrument ID', 'instSerial' : 'Instrument serial', 
                'type' : 'Type', 'friendlyName' : 'Deployment name', 'startDate' : 'Start date', 'endDate' : 'End date'}
    dates_units = ['NA', 'NA', 'NA', 'NA', 'NA', 'UTC', 'UTC']
    dates_df = gen_csv.wrangle_cols(site_deployments_pos_ser, dates_cols, dates_units)

    dates_columns_to_keep = ['Deployment ID', 'instId', 'instSerial', 'suffix', 'type', 'friendlyName', 'startDate', 'endDate']

    #save date file 
    dates_out_name = f"{process_site}_deployment_dates.csv"
    dates_out_dir = os.path.join(network_dir, "deployments", "dates")
    gen_csv.save_to_csv(dates_df, dates_out_dir, dates_out_name)


    ## create position table ## 
    # filter columns for position of deployments
    pos_cols = {'Deployment ID' : 'Deployment ID', 'height' : 'Height', 'yaw' : 'Yaw', 'pitch' : 'Pitch', 
                'roll' : 'Roll'}
    pos_units = ['NA', 'm asl', 'degrees', 'degrees', 'degrees']
    pos_df = gen_csv.wrangle_cols(site_deployments_pos_ser, pos_cols, pos_units)

    #save file 
    pos_out_name = f"{process_site}_deployment_positions.csv"
    pos_out_dir = os.path.join(network_dir, "deployments", "positions")
    gen_csv.save_to_csv(pos_df, pos_out_dir, pos_out_name)

    ## create raw file table ##  
    # filter columns for raw file info of deployments 
    raw_cols = {'Deployment ID' : 'Deployment ID','filenameFormat' : 'Raw file name format', 
                'rawTimeResolution' : 'Raw file time resolution', 'sampleType' : 'Sample type'}
    raw_units = ['NA', 'NA', 'NA', 'Instantaneous/Average']
    raw_df = gen_csv.wrangle_cols(site_deployments_pos_ser, raw_cols, raw_units)

    #save file 
    raw_out_name = f"{process_site}_deployment_raw_files.csv"
    raw_out_dir = os.path.join(network_dir, "deployments", "raw_files")
    gen_csv.save_to_csv(raw_df, raw_out_dir, raw_out_name)

    #get all site ids
    site_inst_ids = list(site_deployments_pos_ser2['instId'])
    ## if a ceilometer has been at site - creat table for profile info ##
    ceil_inst_ids = ['CL31', 'CT25K']
    if any([inst_id in ceil_inst_ids for inst_id in site_inst_ids]):
        # extract scintillometer info
        ceil_deployment_info = site_deployments_pos_ser2[site_deployments_pos_ser2['instId'].isin(ceil_inst_ids)]
        #configure cols
        prof_cols = {'Deployment ID' : 'Deployment ID', 'profileBottom' : 'Profile bottom', 'profileTop' : 'Profile top',
                    'profileStep' : 'Profile step'}
        prof_units = ['NA', 'm asl', 'm asl', 'm asl']
        prof_df = gen_csv.wrangle_cols(ceil_deployment_info, prof_cols, prof_units)
        # save
        prof_out_name = f"{process_site}_profile_deployments.csv"
        prof_out_dir = os.path.join(network_dir, "deployments", "profile_deployments")
        gen_csv.save_to_csv(prof_df, prof_out_dir, prof_out_name)

    ## if a scintillometer has been at site - create a new table for this ## 
    scint_inst_ids = ['BLS', 'LASMKII', 'LAS150']
    if any([inst_id in scint_inst_ids for inst_id in site_inst_ids]):
        # extract scintillometer info
        scint_deployment_info = site_deployments_pos_ser2[site_deployments_pos_ser2['instId'].isin(scint_inst_ids)]
        #config cols
        scint_cols = {'Deployment ID' : 'Deployment ID', 'targetDistance' : 'Target distance',
                    'targetSite' : 'Target site', 'targetHeight' : 'Target height'}
        scint_units = ['NA', 'm', 'NA', 'm asl']
        scint_df = gen_csv.wrangle_cols(scint_deployment_info, scint_cols, scint_units)

        #save 
        scint_out_name = f"{process_site}_scint_deployments.csv"
        scint_out_dir = os.path.join(network_dir, "deployments", "scint_deployments")
        gen_csv.save_to_csv(scint_df, scint_out_dir, scint_out_name)

    ## if an indoor instrument has been at site - create a new table for this ##
    indoor_inst_ids = ['MICROLITE']
    if any([inst_id in indoor_inst_ids for inst_id in site_inst_ids]):
        # extract indoor info
        indoor_deployment_info = site_deployments_pos_ser2[site_deployments_pos_ser2['instId'].isin(indoor_inst_ids)]
        #configure cols
        indoor_cols = {'Deployment ID' : 'Deployment ID', 'roomType' : 'Room type', 'buildingStorey' : 'Building storey', 
                    'distanceToWindow' : 'Distance to wnidow'}
        indoor_units = ['NA', 'NA', 'NA', 'm']
        indoor_df = gen_csv.wrangle_cols(indoor_deployment_info, indoor_cols, indoor_units)

        #save 
        indoor_out_name = f"{process_site}_indoor_deployments.csv"
        indoor_out_dir = os.path.join(network_dir, "deployments", "indoor_deployments")
        gen_csv.save_to_csv(indoor_df, indoor_out_dir, indoor_out_name)
# %%
