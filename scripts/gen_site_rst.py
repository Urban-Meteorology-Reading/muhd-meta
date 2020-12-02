#%%
import os
import math
import pandas as pd
import sqlite3
import io
import gen_rst_functions as gen_rst

#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in site table
site_df = pd.read_sql_query('SELECT * from site', connection)

#close connection
connection.close()
#%%
# get list of all sites 
sites_to_process = site_df['id']

for site in sites_to_process:

    #get the network
    network = site_df.loc[site_df['id'] == site, 'network'].values[0]

    #initiate site file
    site_file_path = os.path.join('..', 'source', 'networks', network, 'sites',)
    site_file_name = f"{site}.rst"
    site_path = os.path.join(site_file_path, site_file_name)
    with io.open(site_path, 'w+', encoding="utf-8") as site_file:
        #write headings
        gen_rst.write_headers(site_file, site)
        #intro
        gen_rst.write_intro(site_file, site)
        #metadata
        gen_rst.write_title(site_file, 'Site metadata')
        gen_rst.write_csv(site_file, f"meta/{site}_meta.csv", 2, stub_columns = True)
        
        #deployments
        #dates
        gen_rst.write_title(site_file, 'Deployments at site')
        gen_rst.write_csv(site_file, f"deployments/dates/{site}_deployment_dates.csv", 2, table_name = 'All site deployments')
        #positions
        gen_rst.write_csv(site_file, f"deployments/positions/{site}_deployment_positions.csv", 2, table_name = 'Position of deployments')
        # raw files
        gen_rst.write_csv(site_file, f"deployments/raw_files/{site}_deployment_raw_files.csv", 2, table_name = 'Raw files of deployments')
        #ceilometer profile
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', "deployments", "profile_deployments", f"{site}_profile_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/profile_deployments/{site}_profile_deployments.csv", 2, table_name = 'Metadata specific to profiles')

        #scint
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', "deployments", "scint_deployments", f"{site}_scint_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/scint_deployments/{site}_scint_deployments.csv", 2, table_name = 'Metadata specific to scintillometers')

        #indoor
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', "deployments", "indoor_deployments", f"{site}_indoor_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/indoor_deployments/{site}_indoor_deployments.csv", 2, table_name = 'Metadata specific to indoor sensors')
        
        #Photos
        #get the photo names and captions required 
        gen_rst.write_title(site_file, 'Photos')
        photo_ref_path = os.path.join('..', 'source', 'networks', network, 'sites', 'photos', site, f'photo_ref.csv')
        if os.path.exists(photo_ref_path):
            photo_ref = pd.read_csv(photo_ref_path)
            photo_ref.apply(lambda x: gen_rst.write_figures(x, site, site_file), axis = 1)
        
        #supplementary info 
        gen_rst.write_title(site_file, 'Supplementary information')
        sup_info_file = os.path.join('..', 'source', 'supplementary_info', 'supplementary_info.csv')
        sup_info = pd.read_csv(sup_info_file)
        # get supplementary info for this site
        site_sup_info = gen_rst.get_supplementary_info(sup_info, 'Site', site)
        
        if len(site_sup_info) > 0:
            site_sup_info = site_sup_info.drop(['Inst Id', 'Site', 'Internal'], axis = 1)
            gen_rst.write_csv_to_list_table(site_file, site_sup_info)
        
        # data_acquisition
        gen_rst.write_title(site_file, "Data acquisition")
        data_acquisition_dir = os.path.join('..', 'source', 'networks', network, 'sites', 'data_acquisition', f'{site}_data_acquisition.rst')
        if os.path.exists(data_acquisition_dir):
            site_file.write(f".. include:: data_acquisition/{site}_data_acquisition.rst\n\n")
        else:
            site_file.write(f".. include:: ../../../data_acquisition/data_acquisition_default.rst\n\n")

        #references
        gen_rst.write_title(site_file, "References")
        ref_dir = os.path.join('..', 'source', 'networks', network, 'sites', 'references', f'{site}_references.csv')
        if os.path.exists(ref_dir):
            gen_rst.write_ref_list(site_file,ref_dir)

        #acknowledgements
        gen_rst.write_title(site_file, "Acknowledgements")
        acknowledgements_path = os.path.join('..', 'source', 'acknowledgements', 'site_acknowledgements.csv')
        gen_rst.write_site_acknowledgements(site_file, acknowledgements_path, site)
# %%
