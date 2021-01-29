#%%
import os
import math
import pandas as pd
import sqlite3
import io
import gen_rst_functions as gen_rst
from write_map_html import *
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
    site_file_path = os.path.join('..', 'source', 'networks', network, 'sites')
    site_file_name = f"{site}.rst"
    site_path = os.path.join(site_file_path, site_file_name)
    with io.open(site_path, 'w+', encoding="utf-8") as site_file:
        # add notes if available
        notes_path = os.path.join('..', 'source', 'supplementary_info', 'notes', 'notes.csv')
        gen_rst.write_notes(site_file, notes_path, site)
        #write headings
        gen_rst.write_headers(site_file, site)
        #intro
        gen_rst.write_intro(site_file, site, site_file_path)
        #metadata
        gen_rst.write_title(site_file, 'Site metadata')
        gen_rst.write_csv(site_file, f"meta/{site}_meta.csv", 1, stub_columns = True)
        #map
        write_map_html(f'../../../_static/network_maps/networks/{network}/{site}_map', site_file)
        #deployments
        #dates
        if os.path.exists(os.path.join(site_file_path, 'deployments', 'dates', f'{site}_deployment_dates.csv')):
            gen_rst.write_title(site_file, 'Deployments at site')
            gen_rst.write_csv(site_file, f"deployments/dates/{site}_deployment_dates.csv", 2, table_name = 'All site deployments')
        
        #positions
        if os.path.exists(os.path.join(site_file_path, 'deployments', 'positions', f'{site}_deployment_positions.csv')):
            gen_rst.write_csv(site_file, f"deployments/positions/{site}_deployment_positions.csv", 2, table_name = 'Position of deployments')
        
        # raw files
        if os.path.exists(os.path.join(site_file_path, 'deployments', 'raw_files', f'{site}_deployment_positions.csv')):
            gen_rst.write_csv(site_file, f"deployments/raw_files/{site}_deployment_raw_files.csv", 2, table_name = 'Raw files of deployments')
        
        #ceilometer profile
        if os.path.exists(os.path.join(site_file_path, "deployments", "profile_deployments", f"{site}_profile_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/profile_deployments/{site}_profile_deployments.csv", 2, table_name = 'Metadata specific to profiles')

        #scint
        if os.path.exists(os.path.join(site_file_path, "deployments", "scint_deployments", f"{site}_scint_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/scint_deployments/{site}_scint_deployments.csv", 2, table_name = 'Metadata specific to scintillometers')

        #indoor
        if os.path.exists(os.path.join(site_file_path, "deployments", "indoor_deployments", f"{site}_indoor_deployments.csv")):
            gen_rst.write_csv(site_file, f"deployments/indoor_deployments/{site}_indoor_deployments.csv", 2, table_name = 'Metadata specific to indoor sensors')
        
        #Photos
        #get the photo names and captions required 
        photo_ref_path = os.path.join(site_file_path, 'photos', site, f'photo_ref.csv')
        if os.path.exists(photo_ref_path):
            gen_rst.write_title(site_file, 'Photos')
            photo_ref = pd.read_csv(photo_ref_path)
            photo_ref.apply(lambda x: gen_rst.write_figures(x, site, site_file), axis = 1)
        
        #supplementary info 
        sup_info_file = os.path.join('..', 'source', 'supplementary_info', 'supplementary_info.csv')
        sup_info = pd.read_csv(sup_info_file)
        # get supplementary info for this site
        site_sup_info = gen_rst.get_supplementary_info(sup_info, 'Site', site)
        
        if len(site_sup_info) > 0:
            gen_rst.write_title(site_file, 'Supplementary information')
            site_sup_info = site_sup_info.drop(['Inst Id', 'Site', 'Internal', 'Make public'], axis = 1)
            gen_rst.write_csv_to_list_table(site_file, site_sup_info)
        
        # data_acquisition
        gen_rst.write_title(site_file, "Data acquisition")
        data_acquisition_dir = os.path.join('..', 'source', 'networks', network, 'sites', 'data_acquisition', f'{site}_data_acquisition.rst')
        if os.path.exists(data_acquisition_dir):
            site_file.write(f".. include:: data_acquisition/{site}_data_acquisition.rst\n\n")
        else:
            site_file.write(f".. include:: ../../../data_acquisition/data_acquisition_default.rst\n\n")
        
        #data availability 
        data_avail_dir = os.path.join( "..", "source", "_static", "availability_plots", f"{site}_availability.html")
        if os.path.exists(data_avail_dir):
            gen_rst.write_title(site_file, "Data availability")
            rel_data_avail_dir = os.path.join("..","..","..","_static","availability_plots",f"{site}_availability.html")
            # wirte an iframe 
            gen_rst.write_data_avail_iframe(site_file, rel_data_avail_dir)
        #references
        ref_dir = os.path.join('..', 'source', 'networks', network, 'sites', 'references', f'{site}_references.csv')
        if os.path.exists(ref_dir):
            gen_rst.write_title(site_file, "References")
            gen_rst.write_ref_list(site_file,ref_dir)

        #acknowledgements
        acknowledgements_path = os.path.join('..', 'source', 'acknowledgements', 'site_acknowledgements.csv')
        gen_rst.write_site_acknowledgements(site_file, acknowledgements_path, site)
# %%
