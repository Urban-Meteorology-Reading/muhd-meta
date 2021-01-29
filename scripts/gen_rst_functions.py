def write_notes(file, notes_path, id):
    '''
    write any notes in notes csv
    '''
    import os
    import pandas as pd
    #check if exists
    if os.path.exists(notes_path):
        notes_df = pd.read_csv(notes_path)
        for index, note_row in notes_df.iterrows():
            all_note_ids = note_row['Page Name'].split(',')
            if id in all_note_ids:
                file.write(".. note::\n")
                file.write(f"   {note_row['Note']}\n\n")
            
def write_headers(file, name):
    '''
    Write the referencer and title of file 
    '''
    #write referencer
    write_referencer(file, name)
    # write title 
    title_overline = len(name) * '*'
    file.write(f"{title_overline}\n{name}\n{title_overline}\n\n")

def write_referencer(file, name):
    '''
    write a referencer
    '''
    file.write(f".. _{name}:\n\n")

def write_title(file, title, symbol = '#'):
    '''
    Write a title 
    '''
    file.write(f"{title}\n{symbol*len(title)}\n\n")

def write_intro(file, name, path):
    '''
    Add intro to rst if one exists
    '''
    import os
    #intro
    if os.path.exists(os.path.join(path, 'intros', f'{name}_intro.rst')):
        write_title(file, 'Introduction')
        file.write(f".. include:: intros/{name}_intro.rst\n\n")

def write_csv(file, file_path, header_rows, table_name = '', stub_columns = False):
    '''
    Write a csv table

    By default it will use headers as the csv header. Set stub_columns to True to use
    index.
    '''
    file.write(f".. csv-table:: {table_name}\n")
    file.write(f"   :file: {file_path}\n")
    if stub_columns == True:
        file.write(f"   :stub-columns: {header_rows}\n\n")
    else:
        file.write(f"   :header-rows: {header_rows}\n\n")

def write_gh_link(file, gh_dir, instId):
    '''
    Extract link to github repo
    '''
    import pandas as pd

    #read csv 
    gh_links = pd.read_csv(gh_dir)
    #extract link for this site 
    inst_gh_link = gh_links[gh_links['Inst ID'] == instId]
    if len(inst_gh_link) > 0: 
        write_title(file, 'Processing code')
        inst_gh_link_write = inst_gh_link['Github URL'].values[0]
        #write 
        file.write(f'Code used to process raw data:\n{inst_gh_link_write}\n\n')

def write_figures(ref_row, id, file):
    '''
    write a row from photo_ref.csv into rst file
    '''
    import math

    file.write(f".. figure:: photos/{id}/{ref_row['name']}\n")

    if math.isnan(ref_row['scale']) == False:
        file.write(f"   :width: {str(int(ref_row['scale']))} %\n")
    
    file.write(f"\n   {ref_row['caption']}\n\n")


def write_csv_to_list_table(file, data, header_rows = 1, table_name = ''):
    '''
    Shared files (more than one page will use data from it) data needs to be selected for relevant page
    '''
    file.write(f".. list-table:: {table_name}\n")
    file.write(f"   :header-rows: {header_rows}\n\n")
    #format the headers currectly
    list_table_headers = '   * - ' + '\n     - '.join(list(data.columns)) + '\n'
    file.write(list_table_headers)
    # write every row 
    data.apply(lambda x: write_list_table_info(x, file), axis = 1)
    file.write("\n")

def write_list_table_info(info_row, file):
    '''
    write a row from suplementary_info.csv into rst file
    '''
    info_row = [str(item) for item in list(info_row)]
    row = '   * - ' + '\n     - '.join(info_row) + '\n'
    file.write(row)

def get_supplementary_info(sup_info, col, id):
    '''
    extract supplementary info for istrument or site (defined by col and id)
    '''
    import pandas as pd
    import math
    
    #init dataframe
    id_sup_info = pd.DataFrame(columns = list(sup_info.columns))
    #for every row
    for index, row in sup_info.iterrows():
        # check for nans
        if type(row[col]) == float:
            if math.isnan(row[col]):
                continue
        # separate by comma 
        all_ids_row = row[col].split(',')
        # append if site/inst id in this row
        if id in all_ids_row:
            if row['Internal'] == True:
                row['Link'] = f":download:`{row['Title']} <{row['Link']}>`"
            # is this to be made public 
            if row['Make public'] == True:
                id_sup_info = id_sup_info.append(row)
        
    return id_sup_info

def write_data_avail_iframe(file, data_avail_dir):
    '''
    Write raw html to embed an iframe data availability plot.
    '''
    # write the raw html required to display a slippy map
    file.write('.. raw:: html\n\n')
    file.write(f'   <iframe src="{data_avail_dir}" height="600px" width="100%" allowfullscreen=true style="border:0px;"></iframe>\n')
    file.write('*Double click on legend to isolate instruments.*\n\n')

def write_ref_list(file, references_path):
    '''
    Write all references as a numbered list 
    '''
    import pandas as pd

    # read in dataframe
    ref_df = pd.read_csv(references_path)
    # loop through references, adding to list 
    for index, row in ref_df.iterrows():
        file.write(f'#. {row["Reference"]}\n')
    
    file.write('\n')

def write_site_acknowledgements(file, acknowledgements_path, site):
    '''
    Get site acknoweldgements from table into written format
    ''' 
    import pandas as pd
    import math

    #read table
    acknowledgements_df = pd.read_csv(acknowledgements_path)
    # check if/where site is in df
    site_acknowledgements_bool = acknowledgements_df['Linked site'].apply(lambda x: site in x if type(x) == str else False) 
    site_acknowledgements = acknowledgements_df[site_acknowledgements_bool]
    site_acknowledgements = site_acknowledgements.drop('Linked site', axis = 1)
    #write to list-table
    if len(site_acknowledgements) > 0:
        #write title
        write_title(file, "Acknowledgements")

        # initiate acknowledgement
        n = 1
        name_str = 'We thank '
        # iterrate through acknowledgements for this site  
        for index, ack in site_acknowledgements.iterrows():
            # if second last item
            if n == (len(site_acknowledgements)-1):
                name_str = name_str + f"{ack['Name/Organisation']} and "
            # if last item
            elif n > (len(site_acknowledgements)-1):
                name_str = name_str + f"{ack['Name/Organisation']} "
            # if middle item
            elif n < (len(site_acknowledgements)-1):
                name_str = name_str + f"{ack['Name/Organisation']}, "
            
            n += 1
        # finalise acknowledgement 
        name_str = name_str + "for site access.\n\n"
        # write acknowledgement
        file.write(name_str)
