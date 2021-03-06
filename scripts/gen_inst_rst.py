#%%
import os
import pandas as pd
import sqlite3
import gen_rst_functions as gen_rst
import io
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in site table
inst_df = pd.read_sql_query('SELECT * from instrument', connection)

#close connection
connection.close()
#%%
# get list of all sites 
insts_to_process = inst_df['instId']

#for every instrument
for instId in insts_to_process:

    #skip blank entry
    if instId == '':
        continue 

    #get the type
    itype = inst_df.loc[inst_df['instId'] == instId, 'type'].values[0]

    inst_file_name = f"{instId}.rst"
    inst_dir = os.path.join('..', 'source', 'instrument_types',itype ,'instIds')
    inst_path = os.path.join(inst_dir, inst_file_name)
    with io.open(inst_path, 'w+', encoding="utf-8") as inst_file:
        # add notes if available
        notes_path = os.path.join('..', 'source', 'supplementary_info', 'notes', 'notes.csv')
        gen_rst.write_notes(inst_file, notes_path, instId)
        #write header 
        gen_rst.write_headers(inst_file, instId)
        #intro
        gen_rst.write_intro(inst_file, instId, inst_dir)
        #manufacturer
        gen_rst.write_title(inst_file, 'Manufacturer and Model')
        gen_rst.write_csv(inst_file, f"manufacturers/{instId}_manufacturer.csv", 1)
        #ouptut definitions
        if os.path.exists(os.path.join(inst_dir, 'out_defs', f'{instId}_out_defs.csv')):
            gen_rst.write_title(inst_file, 'Output definitions')
            gen_rst.write_csv(inst_file, f"out_defs/{instId}_out_defs.csv", 1)
        #code to convert from raw to processed
        gh_dir = os.path.join('..', 'source', 'supplementary_info', 'github_links', 'github_links.csv')
        if os.path.exists(gh_dir):
            gen_rst.write_gh_link(inst_file, gh_dir, instId)
        #variables
        if os.path.exists(os.path.join(inst_dir, 'variables', f'{instId}_variables.csv')):
            gen_rst.write_title(inst_file, 'Variables measured by instrument')
            gen_rst.write_csv(inst_file, f"variables/{instId}_variables.csv", 1, 'Variables measured - sorted alphabetically')
        #serials
        if os.path.exists(os.path.join(inst_dir, 'serials', f'{instId}_serials.csv')):
            gen_rst.write_title(inst_file, 'Serials')
            gen_rst.write_csv(inst_file, f"serials/{instId}_serials.csv", 1)
        #every deployment
        deployment_dir = os.path.join(inst_dir, 'deployments', instId) 
        if os.path.exists(deployment_dir):
            gen_rst.write_title(inst_file, 'Deployments')
            if os.path.exists(deployment_dir):
                all_serials = [i.replace('_deployments.csv', '') for i in os.listdir(deployment_dir)]
                for serial in all_serials:
                    #write referencer
                    inst_file.write(f".. _{serial}:\n\n")
                    gen_rst.write_title(inst_file, f'Serial number: {serial}', '*')
                    gen_rst.write_csv(inst_file, f"deployments/{instId}/{serial}_deployments.csv", 1)

        # photos 
        #get the photo names and captions required 
        photo_ref_path = os.path.join(inst_dir, 'photos', instId, 'photo_ref.csv')
        if os.path.exists(photo_ref_path):
            gen_rst.write_title(inst_file, 'Photos')
            photo_ref = pd.read_csv(photo_ref_path)
            photo_ref.apply(lambda x: gen_rst.write_figures(x, instId, inst_file), axis = 1)

        #supplementary info 
        sup_info_file = os.path.join('..', 'source', 'supplementary_info', 'supplementary_info.csv')
        sup_info = pd.read_csv(sup_info_file)
        # get supplementary info for this inst
        inst_sup_info = gen_rst.get_supplementary_info(sup_info, 'Inst Id', instId)

        if len(inst_sup_info) > 0:
            gen_rst.write_title(inst_file, 'Supplementary information')
            inst_sup_info = inst_sup_info.drop(['Inst Id', 'Site', 'Internal', 'Make public'], axis = 1)
            gen_rst.write_csv_to_list_table(inst_file, inst_sup_info)
        
        #data acquisition
        gen_rst.write_title(inst_file, 'Data acquisition')
        data_acquisition_dir = os.path.join(inst_dir, 'data_acquisition', f'{instId}_data_acquisition.rst')
        if os.path.exists(data_acquisition_dir):
            inst_file.write(f".. include:: data_acquisition/{instId}_data_acquisition.rst\n\n")
        else:
            inst_file.write(f".. include:: ../../../data_acquisition/data_acquisition_default.rst\n\n")
        
        #references
        ref_dir = os.path.join(inst_dir, 'references', f'{instId}_references.csv')
        if os.path.exists(ref_dir):
            gen_rst.write_title(inst_file, 'References')        
            gen_rst.write_ref_list(inst_file,ref_dir)
# %%
