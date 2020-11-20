#%%
import os
import math
import pandas as pd
import sqlite3
#%%
def write_figures(ref_row, site, site_file):
    '''
    write a row from photo_ref.csv into rst file
    '''

    site_file.write(f".. figure:: photos/{site}/{ref_row['name']}\n")

    if math.isnan(ref_row['scale']) == False:
        site_file.write(f"   :scale: {str(int(ref_row['scale']))}\n")
    
    site_file.write(f"\n   {ref_row['caption']}\n\n")
# %%
def write_sup_info(sup_info_row, site_file):
    '''
    write a row from suplementary_info.csv into rst file
    '''
    site_file.write(f"   * - {sup_info_row['Link']}\n     - {sup_info_row['Title']}\n     - {sup_info_row['Description']}\n")
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
    with open(site_path, 'w+') as site_file:
        #write referencer
        site_file.write(f".. _{site}:\n\n")
        # write title 
        title = len(site) * '*'
        site_file.write(f"{title}\n{site}\n{title}\n\n")
        #intro
        site_file.write(f"Introduction\n{'#'*12}\n\n")
        site_file.write(f".. include:: intros/{site}_intro.rst\n\n")
        #metadata
        site_file.write(f"Site metadata\n{'#'*13}\n\n")
        site_file.write(f".. csv-table::\n")
        site_file.write(f"   :file: meta/{site}_meta.csv\n")
        site_file.write(f"   :stub-columns: 2\n\n")
        
        #deployments
        #dates
        site_file.write(f"Deployments at site\n{'#'*19}\n\n")
        site_file.write(f".. csv-table:: All site deployments\n")
        site_file.write(f"   :file: deployments/dates/{site}_deployment_dates.csv\n")
        site_file.write(f"   :header-rows: 2\n\n")
        #positions
        site_file.write(f".. csv-table:: Position of deployments\n")
        site_file.write(f"   :file: deployments/positions/{site}_deployment_positions.csv\n")
        site_file.write(f"   :header-rows: 2\n\n")
        # raw files
        site_file.write(f".. csv-table:: Raw files of deployments\n")
        site_file.write(f"   :file: deployments/raw_files/{site}_deployment_raw_files.csv\n")
        site_file.write(f"   :header-rows: 2\n\n")
        #scint
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', "deployments", "scint_deployments", f"{site}_scint_deployments.csv")):
            site_file.write(f".. csv-table:: Metadata specific to scintillometers\n")
            site_file.write(f"   :file: deployments/scint_deployments/{site}_scint_deployments.csv\n")
            site_file.write(f"   :header-rows: 2\n\n")
        #indoor
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', "deployments", "indoor_deployments", f"{site}_indoor_deployments.csv")):
            site_file.write(f".. csv-table:: Metadata specific to indoor sensors\n")
            site_file.write(f"   :file: deployments/indoor_deployments/{site}_indoor_deployments.csv\n")
            site_file.write(f"   :header-rows: 2\n\n")
        
        #Photos
        #get the photo names and captions required 
        site_file.write(f"Photos\n{'#'*6}\n\n")
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', 'photos', site, f'{site}_photo_ref.csv')):
            photo_ref = pd.read_csv(os.path.join('..', 'source', 'network', network, 'sites', 'photos', site, f'{site}_photo_ref.csv'))
            photo_ref.apply(lambda x: write_figures(x, site, site_file), axis = 1)

        #supplementary info
        site_file.write(f"Supplementary information\n{'#'*25}\n\n")
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', 'supplementary_info', 'supplementary_info.csv')):
            sup_info = pd.read_csv(os.path.join('..', 'source', 'networks', network, 'sites', 'supplementary_info', 'supplementary_info.csv'))
            site_sup_info = sup_info[sup_info['Site'] == site]
            if len(site_sup_info) > 0:
                site_file.write(f".. list-table::\n")
                site_file.write(f"   :header-rows: 1\n\n")
                site_file.write(f"   * - Link\n     - Title\n     - Description\n")
                site_sup_info.apply(lambda x: write_sup_info(x, site_file), axis = 1)
                site_file.write("\n")
        
        # data_acquisition
        site_file.write(f"Data acquisition\n{'#'*16}\n\n")
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', 'data_acquisition', 'data_acquisition.csv')):
            print('Get data_acquisition info here')
        
        #references
        site_file.write(f"References\n{'#'*10}\n\n")
        if os.path.exists(os.path.join('..', 'source', 'networks', network, 'sites', 'references', 'references.csv')):
            print('Get references here')
# %%
