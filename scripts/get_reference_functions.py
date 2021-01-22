def read_additions_omissions(ref_om_ad_dir):
    '''
    Read in ommissions and additions csvs
    '''
    import os
    import pandas as pd
    
    # file paths
    omit_csv_path = os.path.join(ref_om_ad_dir, 'reference_omissions.csv')
    add_csv_path = os.path.join(ref_om_ad_dir, 'reference_additions.csv')
    # read in omissions csv
    if os.path.exists(omit_csv_path):
        omit_df = pd.read_csv(omit_csv_path)
        omit_df_exists = True
    else:
        omit_df_exists = False

    # read in additions csv
    if os.path.exists(add_csv_path):
        add_df = pd.read_csv(add_csv_path, encoding='cp1252')
        add_df_exists = True
    else:
        add_df_exists = False
    
    return omit_df, omit_df_exists, add_df, add_df_exists

def get_new_site_inst(site_inst):
    ''' 
    manually alter site inst used for searching
    '''
    #change LASMKII to LAS MKII
    if site_inst == 'LASMKII':
        site_inst_new = 'LAS+MKII'
    # add scintillometer to bls search 
    elif site_inst == 'BLS':
        site_inst_new = 'BLS%2C+scintillometer'
    # temperature probe for swt 
    elif site_inst == '107':
        site_inst_new = '107+campbell+SWT'
    #bh indoor site
    elif site_inst == 'BH':
        site_inst_new = 'BH+barford'
    #ch indoor site
    elif site_inst == 'CH':
        site_inst_new = 'CH+council+house'
    #oh indoor site
    elif site_inst == 'OH':
        site_inst_new = 'OH+orford+house'
    #rh indoor site
    elif site_inst == 'RH':
        site_inst_new = 'RH+rahere+house'
    #HAN site
    elif site_inst == 'HAN':
        site_inst_new = 'HAN+Hanover'
    #MT site
    elif site_inst == 'MT':
        site_inst_new = 'MT+Middle+temple'
    #TEM site
    elif site_inst == 'TEM':
        site_inst_new = 'TEM+Victoria+embankment+temple'
    #CT site
    elif site_inst == 'CT':
        site_inst_new = 'CT+Tokyo+central+tower'
    #LI7500A sometimes missing the A
    elif site_inst == 'LI7500A':
        site_inst_new = 'LI7500'
    # gill needs just Gill R3 search
    elif site_inst == 'GILL121R03':
        site_inst_new = 'Gill+R3'
    # PAR needs to be more specific
    elif site_inst == 'PAR':
        site_inst_new = 'PAR+SKYE'
    # Pi160 needs to be less specific
    elif site_inst == 'PI160':
        site_inst_new = 'otris'
    # omega thermocouple
    elif site_inst == 'THERMOCOUPLE':
        site_inst_new = 'Thermocouple+omega'
    # davis is too general
    elif site_inst == 'DAVIS':
        site_inst_new = 'Davis+vantage'
    else:
        site_inst_new = site_inst

    return site_inst_new 

def get_search_str(search_type, author = None, site_inst_new = None, centaur_id = None):
    '''
    Get URL after base_url
    '''
    # urls differ for site and inst
    if search_type == 'inst':
        exp = ("0%7C1%7C-date%2Fcreators_sort_name%2Ftitle%7Carchive%7C-%7Cnas_fulltext%3Adocuments%3AALL"
                f"%3AIN%3A{site_inst_new}%7Cnas_multiname%3Aconductors_name%2Fcontributors_name%2Fcreators_name%"
                f"2Feditors_name%2Flyricists_name%2Fproducers_name%3AALL%3AEQ%3A{author}%7C-%7Ceprint_status%"
                "3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow")
    elif search_type == 'site':
        exp = (f"exp=0%7C1%7C%7Carchive%7C-%7Cq%3A%3AALL%3AIN%3A{author}+{site_inst_new}%7C-%7C")
    elif search_type == 'centaur_id':
        exp = (f"0%7C1%7C-date%2Fcreators_sort_name%2Ftitle%7Carchive%7C-%7Cnas_itemid%3Aeprintid%3AALL%3AEQ%3A{centaur_id}"
               "%7C-%7Ceprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow")
    else:
        raise ValueError('search_type must equal either "site", "inst" or "centaur_id"') 

    return exp

def create_search_url(exp, base_url_adv, base_url_simp, search_type):
    '''
    generate the url to sent to centaur
    '''

    #decide whether to use advanced or simple search - this changes the outcome
    if search_type == 'inst' or search_type == 'centaur_id':
        base_url = base_url_adv
    elif search_type == 'site':
        base_url = base_url_simp

    # define parameters to use
    params = {'screen' : 'Search', 
            'dataset' : 'archive', 
            '_action_export' : '1',
            'output' : 'IDandHTML',
            'exp' : exp,
            'n' : '',
            'cache' : ''}
    #join keys, values
    url_string_list = []
    for key, value in params.items():
        url_string_list.append('='.join([key,value])) 
    #url params joined by & 
    url_params = '&'.join(url_string_list)
    request_url = f"{base_url}?{url_params}"

    return request_url

def submit_parse(request_url):
    '''
    submit request to centaur - initial format
    '''
    from bs4 import BeautifulSoup
    import requests

    #submit to centaur to get id and title
    response = requests.get(request_url)
    #parse text
    references = response.text

    # parse html
    ref_html = BeautifulSoup(references, 'html.parser')

    return ref_html

def decode_html(ref_html, site_inst, omit_df_exists, omit_df = None):
    '''
    Convert from html to df
    '''
    import re 
    import pandas as pd

    # extract all p tags
    html_refs = ref_html.find_all('p')
    # init df 
    ref_cols = ['eprint_id', 'Reference', 'year']
    ref_df = pd.DataFrame(columns=ref_cols)
    # loop through every reference and append to df
    for ref in html_refs:
        # format 
        ref_list = ref.get_text().split('|')
        ref_list = [text.strip().replace('\n', ' ').replace('\r', ' ') for text in ref_list]
        ref_list[1] = re.sub(' +', ' ', ref_list[1])

        #check if this should be omitted
        if omit_df_exists == True:
            site_inst_omit = omit_df[omit_df['Page Name'] == site_inst]
            #centaur id
            cent_ref_list = int(ref_list[0])
            # skip if need to omit
            if cent_ref_list in site_inst_omit['Centaur ID'].values:
                continue

        #extract the year 
        ref_year = []
        # loop through potential year locations (location changes depending on publication type)
        for i in ref.find_all('span'):
            next_sib = i.next_sibling
            try:
                yr = int(re.findall(r'\d+', next_sib.strip())[0])
                ref_year.append(yr)
            except:
                continue
        #check if a value is feasibly a date
        ref_year_filt = [i for i in ref_year if 1900 < i < 2100]
        #check if more than one fits criteria - give warning
        if len(ref_year_filt) > 1:
            print((f"eprint id: {str(ref_list[0])} found more than one date when attempting to parse date." 
                    f" Found {', '.join([str(i) for i in ref_year_filt])}. Will select {str(ref_year_filt[0])}."))
        year = ref_year_filt[0]
        # append to df 
        ref_list.append(year)
        ref_series = pd.Series(ref_list, index = ref_cols)
        ref_df = ref_df.append(ref_series, ignore_index = True)

    return ref_df

def extract_references(search_type, author, site_inst_new, site_inst, base_url_adv, base_url_simp, omit_df_exists, omit_df, centaur_id = None):
        #get search url after base url
        exp = get_search_str(search_type, author = author, site_inst_new = site_inst_new, centaur_id = centaur_id )
        #get full url to request 
        request_url = create_search_url(exp, base_url_adv, base_url_simp, search_type)
        #submit to centaur - return html
        ref_html = submit_parse(request_url)
        # convert to dataframe
        ref_df = decode_html(ref_html, site_inst, omit_df_exists, omit_df)

        return ref_df

def check_ref_df(add_ref_df,add_ref_row):
    #check if it found the reference (was id valid)
    if len(add_ref_df) > 0:
        print(f"Adding reference from {str(int(add_ref_row['Centaur ID']))}")
        add_ref_series = add_ref_df.iloc[0]
    else:
        print(f"{add_ref_row['Centaur ID']} centaur id found to be invalid.")
        add_ref_series = add_ref_df
    
    return add_ref_series

def get_add_ref(add_ref_row, base_url_adv, base_url_simp):
    '''
    Add a manually added reference 
    '''

    import math 
    import pandas as pd

    # if we're not given the details 
    if pd.isna(add_ref_row['Full reference']) and pd.isna(add_ref_row['Centaur ID']):
        print('Please enter a Centaur ID or full reference')
        add_ref_series = pd.Series(index = ['eprint_id', 'Reference', 'year'])
    # if only centaur id is given 
    elif pd.isna(add_ref_row['Full reference']) and (pd.isna(add_ref_row['Centaur ID']) == False):
        print('Attempting to source using centaur id')
        # search for id
        add_ref_df = extract_references('centaur_id', None, None, None, base_url_adv, base_url_simp, False, None, str(int(add_ref_row['Centaur ID'])))
        #check if we're given a valid return
        add_ref_series = check_ref_df(add_ref_df, add_ref_row)
    # if full reference given
    elif pd.isna(add_ref_row['Full reference']) == False:
        # if year is given - add this in
        if pd.isna(add_ref_row['Year']) == False:
            add_ref_series = pd.Series({'eprint_id': None, 
                                        'Reference' : add_ref_row['Full reference'], 
                                        'year': int(add_ref_row['Year'])})
        #if no year
        else:
            print('No year provided for full reference')
            # try using centaru id if given
            if pd.isna(add_ref_row['Centaur ID']) == False:
                print('Attempting to source using centaur id')
                add_ref_df = extract_references('centaur_id', None, None, None, base_url_adv, base_url_simp, False, None, str(int(add_ref_row['Centaur ID'])))
                #check if a reference has been returned
                add_ref_series = check_ref_df(add_ref_df, add_ref_row)
            # give up
            else:
                print('Cannot add reference')
                # return empty 
                add_ref_series = pd.Series(index = ['eprint_id', 'Reference', 'year'])

    return add_ref_series

def get_references(base_url_adv, base_url_simp, site_inst, author, search_type, out_dir, omit_df_exists, omit_df, add_df_exists, add_df):
    '''
    Search centaur for references on a specific site or instrument
    '''
    import os
    import pandas as pd
    
    # manually get new search parameter 
    site_inst_new = get_new_site_inst(site_inst)
    # extract all references for this site/inst from centaur and format into df
    ref_df = extract_references(search_type, author, site_inst_new, site_inst, base_url_adv, base_url_simp, omit_df_exists, omit_df)

    #omit non Grimmond papers (or Kent thesis)
    ref_df = ref_df[ref_df['Reference'].str.contains('Grimmond') | ref_df['Reference'].str.contains('Kent')]
    # check for additions
    if add_df_exists:
        if site_inst in add_df['Page Name'].values:
            site_inst_add = add_df[add_df['Page Name'] == site_inst]
            added_ref_df = site_inst_add.apply(lambda x: get_add_ref(x, base_url_adv, base_url_simp), axis = 1)
            ref_df = pd.concat([ref_df, added_ref_df], axis = 0)
    # sort by year - 
    ref_df = ref_df.sort_values('year', ascending = False)
    #define out dir
    ref_dir = out_dir
    if os.path.exists(ref_dir) == False:
        os.makedirs(ref_dir)
    ref_file_name =  f'{site_inst}_references.csv'
    ref_file_path = os.path.join(ref_dir, ref_file_name)
    # remove if already exists
    if os.path.exists(ref_file_path):
        os.remove(ref_file_path)
    #write
    if len(ref_df) > 0:
        ref_df.to_csv(ref_file_path, index = False)