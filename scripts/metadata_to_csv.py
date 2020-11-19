#%%
import sqlite3
import pandas as pd
import os 
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
process_site = 'RGS'

#%%
#get the site meta
process_site_info = site.loc[site['id'] == process_site].T

#renane cols, get units 
process_site_info = process_site_info.rename(index = {'id' : 'Site ID', 'fullName' : 'Full Name', 'network' : 'Network',
                                   'longitude' : 'Longitude', 'latitude' : 'Latitude', 'startDate' : 'Start date', 
                                   'endDate' : 'End date', 'displacementHeight' : 'Displacement height', 'city' : 'City'})
site_cols_units = pd.MultiIndex.from_arrays([list(process_site_info.index), 
                    ['NA', 'NA', 'NA', 'degrees', 'degrees', 'UTC', 'UTC', 'm', 'NA']])
process_site_info.index = site_cols_units

#save the site meta
meta_out_name = f"{process_site}_meta.csv"
meta_out_dir = os.path.join("..", "source", "LUMA", "sites", "meta")
meta_out_dir_name = os.path.join(meta_out_dir, meta_out_name)

process_site_info.to_csv(meta_out_dir_name, header = False)

#%%
# get deployment info at site
site_deployments = deployment[deployment['siteId'] == process_site]
site_deployments_pos = site_deployments.merge(position, left_on = 'id', right_on = 'deploymentId')
site_deployments_pos_ser = site_deployments_pos.merge(instSerial, left_on = 'instSerial', right_on = 'serial')
#%%
# format dates to only include time
site_deployments_pos_ser['startDate'] = site_deployments_pos_ser['startDate'].apply(lambda x: x.split(' ')[0])
site_deployments_pos_ser['endDate'] = site_deployments_pos_ser['endDate'].apply(lambda x: x.split(' ')[0] if x != None else x)
# add a column for dployment id 
site_deployments_pos_ser['Deployment ID'] = [f"{process_site}_{n}" for n in range(len(site_deployments_pos_ser))]

#%%
#remove SWTWXSTATION id from SWT table (this is required for processing but not very accurate)
if process_site == 'SWT':
    site_deployments_pos_ser = site_deployments_pos_ser.loc[site_deployments_pos_ser['instId'] != 'SWTWXSTATION']
#%%
# filter columns for date of deployments 
dates_columns_to_keep = ['Deployment ID', 'instId', 'instSerial', 'suffix', 'type', 'friendlyName', 'startDate', 'endDate']
# dps - deployments, position, serial tables
dates_df = site_deployments_pos_ser[dates_columns_to_keep]

#rename cols, add units
dates_df = dates_df.rename(columns = {'instId' : 'Instrument ID', 'instSerial' : 'Instrument serial', 'suffix' : 'Letter',
                                    'type' : 'Type', 'friendlyName' : 'Deployment name', 'startDate' : 'Start date', 
                                    'endDate' : 'End date'})
dates_cols_units = pd.MultiIndex.from_arrays([list(dates_df.columns), 
                    ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'UTC', 'UTC']])
dates_df.columns = dates_cols_units
#save date file 
dates_out_name = f"{process_site}_deployment_dates.csv"
dates_out_dir = os.path.join("..", "source", "LUMA", "sites", "deployments", "dates")
dates_out_dir_name = os.path.join(dates_out_dir, dates_out_name)
dates_df.to_csv(dates_out_dir_name, index = False)
#%%
#create position table 
# filter columns for date of deployments 
pos_columns_to_keep = ['Deployment ID', 'height', 'yaw', 'pitch', 'roll']
# dps - deployments, position, serial tables
pos_df = site_deployments_pos_ser[pos_columns_to_keep]
# rename cols, add units
pos_df = pos_df.rename(columns = {'height' : 'Height', 'yaw' : 'Yaw', 'pitch' : 'Pitch', 
                                    'roll' : 'Roll'})
pos_cols_units = pd.MultiIndex.from_arrays([list(pos_df.columns), 
                    ['NA', 'm asl', 'degrees', 'degrees', 'degrees']])
pos_df.columns = pos_cols_units
#save file 
pos_out_name = f"{process_site}_deployment_positions.csv"
pos_out_dir = os.path.join("..", "source", "LUMA", "sites", "deployments", "positions")
pos_out_dir_name = os.path.join(pos_out_dir, pos_out_name)
pos_df.to_csv(pos_out_dir_name, index = False)
#%%
#create raw file table 
# filter columns for date of deployments 
raw_columns_to_keep = ['Deployment ID', 'filenameFormat', 'rawTimeResolution', 'sampleType']
# extract cols
raw_df = site_deployments_pos_ser[raw_columns_to_keep]
# rename cols, add units
raw_df = raw_df.rename(columns = {'filenameFormat' : 'Raw file name format', 'rawTimeResolution' : 'Raw file time resolution',
                                  'sampleType' : 'Sample type'})
raw_cols_units = pd.MultiIndex.from_arrays([list(raw_df.columns), 
                    ['NA', 'NA', 'NA', 'Instantaneous/Average']])
raw_df.columns = raw_cols_units
#save file 
raw_out_name = f"{process_site}_deployment_raw_files.csv"
raw_out_dir = os.path.join("..", "source", "LUMA", "sites", "deployments", "raw_files")
raw_out_dir_name = os.path.join(raw_out_dir, raw_out_name)
raw_df.to_csv(raw_out_dir_name, index = False)
#%%
# if a scintillometer has been at site - create a new table for this
scint_inst_ids = ['BLS', 'LASMKII', 'LAS150']
site_inst_ids = list(site_deployments_pos_ser['instId'])
if any([inst_id in scint_inst_ids for inst_id in site_inst_ids]):
    # extract scintillometer info
    scint_deployment_info = site_deployments_pos_ser[site_deployments_pos_ser['instId'].isin(scint_inst_ids)]
    # keep scint specific cols    
    scint_columns_to_keep = ['Deployment ID', 'targetDistance', 'targetSite', 'targetHeight']
    scint_deployment_info = scint_deployment_info[scint_columns_to_keep]
    #rename, add units
    scint_deployment_info = scint_deployment_info.rename(columns = {'targetDistance' : 'Target distance',
                                        'targetSite' : 'Target site', 'targetHeight' : 'Target height'})
    scint_cols_units = pd.MultiIndex.from_arrays([list(scint_deployment_info.columns), 
                        ['NA', 'm', 'NA', 'm asl']])
    scint_deployment_info.columns = scint_cols_units
    
    #save 
    scint_out_name = f"{process_site}_scint_deployments.csv"
    scint_out_dir = os.path.join("..", "source", "LUMA", "sites", "deployments", "scint_deployments")
    scint_out_dir_name = os.path.join(scint_out_dir,scint_out_name)
    scint_deployment_info.to_csv(scint_out_dir_name, index = False)

#%%
# if a indoor instrument has been at site - create a new table for this
indoor_inst_ids = ['MICROLITE']
site_inst_ids = list(site_deployments_pos_ser['instId'])
if any([inst_id in indoor_inst_ids for inst_id in site_inst_ids]):
    # extract indoor info
    indoor_deployment_info = site_deployments_pos_ser[site_deployments_pos_ser['instId'].isin(indoor_inst_ids)]
    # keep indoor specific cols    
    indoor_columns_to_keep = ['Deployment ID', 'roomType', 'buildingStorey', 'distanceToWindow']
    indoor_deployment_info = indoor_deployment_info[indoor_columns_to_keep]
    #rename, add units
    indoor_deployment_info = indoor_deployment_info.rename(columns = {'roomType' : 'Room type', 'buildingStorey' : 'Building storey', 
                                                                      'distanceToWindow' : 'Distance to wnidow'})
    indoor_cols_units = pd.MultiIndex.from_arrays([list(indoor_deployment_info.columns), 
                        ['NA', 'NA', 'NA', 'm']])
    indoor_deployment_info.columns = indoor_cols_units
    
    #save 
    indoor_out_name = f"{process_site}_indoor_deployments.csv"
    indoor_out_dir = os.path.join("..", "source", "LUMA", "sites", "deployments", "indoor_deployments")
    indoor_out_dir_name = os.path.join(indoor_out_dir,indoor_out_name)
    indoor_deployment_info.to_csv(indoor_out_dir_name, index = False)
# %%
