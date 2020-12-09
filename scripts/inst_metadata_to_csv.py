#%%
import os
import math
import pandas as pd
import sqlite3
import gen_csv_functions as gen_csv
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in tables
instrument = pd.read_sql_query('SELECT * from instrument', connection)
serial = pd.read_sql_query('SELECT * from instSerial', connection)
out_def = pd.read_sql_query('SELECT * from outDef', connection)
out_def_level = pd.read_sql_query('SELECT * from outDefLevel', connection)
out_def_TR = pd.read_sql_query('SELECT * from outDefTimeRes', connection)
out_def_var = pd.read_sql_query('SELECT * from outDefVariable', connection)
out_def_parent_var = pd.read_sql_query('SELECT * from outDefParentVariable', connection)
variable = pd.read_sql_query('SELECT * from variable', connection)
deployment = pd.read_sql_query('SELECT * from deployment', connection)
position = pd.read_sql_query('SELECT * from position', connection)
site = pd.read_sql_query('SELECT * from site', connection)

#close connection
connection.close()
#%%
insts_to_process = instrument['instId']

for instId in insts_to_process:
    
    #skip blank entry
    if instId == '':
        continue 

    print(instId)
    #get the type
    itype = instrument.loc[instrument['instId'] == instId, 'type'].values[0]
    #init dirs
    inst_out_dir = os.path.join('..', 'source', 'instrument_types', itype, 'instIds')
    if os.path.exists(inst_out_dir) == False:
        os.makedirs(inst_out_dir)

    # metadata for instrument
    inst_info = instrument.loc[instrument['instId'] == instId]
    inst_col_format = {'model' : 'Model', 'brand' : 'Brand', 'type' : 'Type'}
    inst_info = gen_csv.wrangle_cols(inst_info, inst_col_format)
    #save 
    inst_info_dir = os.path.join(inst_out_dir, 'manufacturers')
    inst_info_name = f"{instId}_manufacturer.csv"
    gen_csv.save_to_csv(inst_info, inst_info_dir, inst_info_name)

    #get file identifiers and levels 
    inst_out_def = out_def.loc[out_def['instId'] == instId]
    if len(inst_out_def) > 0: 
        inst_out_def_lev = inst_out_def.merge(out_def_level, left_on = 'id', right_on = 'defId')
        # lt level & time
        inst_out_def_lt = inst_out_def_lev.merge(out_def_TR, on = 'defId')
        #here filter 3sec l1 and 15sec l0 cl31
        if instId == 'CL31':
            inst_out_def_lt = inst_out_def_lt.loc[~((inst_out_def_lt['levelNum'] == 0) & (inst_out_def_lt['timeRes'] == '15sec') & (inst_out_def_lt['defId'] == 'CL31_BSC'))]
            inst_out_def_lt = inst_out_def_lt.loc[~((inst_out_def_lt['levelNum'] == 1) & (inst_out_def_lt['timeRes'] == '3sec') & (inst_out_def_lt['defId'] == 'CL31_BSC'))]

        # re-format columns
        inst_out_def_lt_col_format = {'defId' : 'Ouput definition ID', 'fileIdentifier' : 'File Identifier', 'levelNum' : 'Level Number',
                                                'QAQC' : 'QAQC notes', 'timeRes' : 'File time resolution'}
        inst_out_def_lt_filter = gen_csv.wrangle_cols(inst_out_def_lt, inst_out_def_lt_col_format)
        #save 
        out_defs_dir = os.path.join(inst_out_dir, 'out_defs')
        out_defs_name = f"{instId}_out_defs.csv"
        gen_csv.save_to_csv(inst_out_def_lt_filter, out_defs_dir, out_defs_name)

        # variables measured by this instrument
        #merge the tables
        inst_out_def_ltv = inst_out_def_lt.merge(out_def_var, left_on = 'id_y', right_on = 'levelId')
        inst_out_def_ltvv = inst_out_def_ltv.merge(variable, left_on = 'variableId', right_on = 'id')
        
        if len(inst_out_def_ltvv) > 0:
            # create column of outdef Id, level, time res
            inst_out_def_ltvv['outDefs'] = inst_out_def_ltvv.apply(lambda x: x['defId'] + ',' + str(x['levelNum']) + ',' + x['timeRes'], axis = 1)
            inst_vars = inst_out_def_ltvv.groupby(['variableId', 'fullName', 'unit', 'lowerThreshold', 'upperThreshold']).apply(lambda x: ' '.join(x['outDefs']))
            inst_vars = inst_vars.reset_index(name = 'OutDefs')
            # name cols
            inst_vars_col_format = {'variableId' : 'Variable ID', 'fullName' : 'Full Name', 'unit' : 'Unit',
                                                    'lowerThreshold' : 'Lower Threshold', 'upperThreshold' : 'Upper Threshold', 
                                                    'OutDefs' : 'Files present (Output definition ID,Level No,Time resolution)'}
            inst_vars = gen_csv.wrangle_cols(inst_vars, inst_vars_col_format)
            # sort alphabetically 
            inst_vars = inst_vars.loc[inst_vars['Variable ID'].str.lower().sort_values().index]
            #save 
            vars_dir = os.path.join(inst_out_dir, 'variables')
            vars_name = f"{instId}_variables.csv"
            gen_csv.save_to_csv(inst_vars, vars_dir, vars_name)
        else:
            print('No variables found')
    else:
        print('Instrument has no output definitions')

    # serials of instruments
    inst_serials = serial.loc[serial['instId'] == instId]
    if len(inst_serials) > 0:
        inst_serials['serial'] = inst_serials['serial'].apply(lambda x: f":ref:`{x}`")
        inst_serials = gen_csv.wrangle_cols(inst_serials, {'serial' : 'Serial', 'suffix' : 'Suffix'})
        inst_serials = inst_serials.sort_values('Suffix')
        #save 
        serial_dir = os.path.join(inst_out_dir, 'serials')
        serial_name = f"{instId}_serials.csv"

        gen_csv.save_to_csv(inst_serials, serial_dir, serial_name)

        # deployments of every instrument 
        deployments_pos = deployment.merge(position, left_on = 'id', right_on = 'deploymentId')
        deployments_pos_ser = deployments_pos.merge(serial, left_on = 'instSerial', right_on = 'serial')
        inst_deployments = deployments_pos_ser[deployments_pos_ser['instId'] == instId]
        if len(inst_deployments) >0:
            #reference site 
            inst_deployments['siteId'] = inst_deployments['siteId'].apply(lambda x: f":ref:`{x}`")
            # filter columns
            depl_cols_format = {'serial' : 'Serial', 'siteId' : 'Site ID', 'startDate' : 'Start date', 'endDate' : 'End date'}
            inst_deployments = gen_csv.wrangle_cols(inst_deployments, depl_cols_format)

            #save each serials deployments in a table
            depl_dir = os.path.join(inst_out_dir, 'deployments', instId)
            # for every serial
            inst_deployments_g = inst_deployments.groupby('Serial')
            for serial_no, group in inst_deployments_g:
                # format information
                group_out = group.drop('Serial', axis = 1)
                group_out = group_out.sort_values(by='Start date')
                #save 
                #replace ML2 slash with underscore (or cannot save)
                if serial_no == "224/063":
                    serial_no = serial_no.replace('/', '_')
                depl_ser_name = f"{serial_no}_deployments.csv"
                gen_csv.save_to_csv(group_out, depl_dir, depl_ser_name)
        else:
            print('No deployments of instrument')
    else:
        print('No serials for instrument')

# %%
