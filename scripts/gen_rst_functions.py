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

def write_intro(file, name):
    '''
    Add intro to rst
    '''
    #intro
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

def wrtie_gh_link(file, gh_dir, instId):
    '''
    Extract link to github repo
    '''
    import pandas as pd

    #read csv 
    gh_links = pd.read_csv(gh_dir)
    #extract link for this site 
    inst_gh_link = gh_links[gh_links['Instrument ID'] == instId]
    if len(inst_gh_link) > 0: 
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
        file.write(f"   :scale: {str(int(ref_row['scale']))}\n")
    
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
            id_sup_info = id_sup_info.append(row)
        
    return id_sup_info

def write_site_acknowledgements(file, acknowledgements_path, site):
    '''
    Get site acknoweldgements from table into written format
    ''' 
    import pandas as pd
    import math

    #read table
    acknowledgements_df = pd.read_csv(acknowledgements_path)
    site_acknowledgements = acknowledgements_df[acknowledgements_df['Linked site'] == site]
    site_acknowledgements = site_acknowledgements.drop('Linked site', axis = 1)
    #write to list-table
    if len(site_acknowledgements) > 0:
        file.write(f"We thank ")
        site_acknowledgements_group = site_acknowledgements.groupby('Organisation')
        n_orgs = len(site_acknowledgements['Organisation'].unique())
        n = 1
        for org, group in site_acknowledgements_group:
            #check if it is organisation only
            if all([str(names) != 'nan' for names in group['Name']]):
                file.write(f"{', '.join(group['Name'])} from {org}")
            else:
                file.write(f"{org}")
            #if last org add a space
            if n == n_orgs:
                file.write(' ')
            # if second last write and
            elif n_orgs - n == 1:
                file.write(' and ')
            #else separate with comma
            else:
                file.write(', ')
            n += 1
        file.write(f"for initial and continued site access.\n\n")
