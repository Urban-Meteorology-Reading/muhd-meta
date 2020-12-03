# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:28:54 2020

@author: kitbe
"""
#%%
import requests
import os
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
import re
#%%
#author in search parameters 
author = 'Grimmond'
#base url to submit to for instruments and sites - simple search works best for sites and advanced for inst - advanced tends to find too few and simple too many
base_url_inst = 'http://centaur.reading.ac.uk/cgi/search/archive/advanced/export_reading_IDandHTML.html'
base_url_site = "http://centaur.reading.ac.uk/cgi/search/archive/simple/export_reading_IDandHTML.html"
# out directory for instruments
inst_out_dir = os.path.join('..','source','instruments','instIds','references')
# out directory for sites
site_out_dir = os.path.join('..','source','networks')
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in site table
site_df = pd.read_sql_query('SELECT * from site', connection)
inst_df = pd.read_sql_query('SELECT * from instrument', connection)

#close connection
connection.close()
#%% 
def get_references(base_url, site_inst, author, search_type, out_dir, network = None):
    
    #change LASMKII to LAS MKII
    if site_inst == 'LASMKII':
        site_inst_new = 'LAS+MKII'
    # add scintillometer to bls search 
    elif site_inst == 'BLS':
        site_inst_new = 'BLS%2C+scintillometer'
    # temperature probe for swt 
    elif site_inst == '107':
        site_inst_new = '107+campbell+SWT'
    else:
        site_inst_new = site_inst

    # urls differ for site and inst
    if search_type == 'inst':
        exp = ("0%7C1%7C-date%2Fcreators_sort_name%2Ftitle%7Carchive%7C-%7Cnas_fulltext%3Adocuments%3AALL"
                f"%3AIN%3A{site_inst_new}%7Cnas_multiname%3Aconductors_name%2Fcontributors_name%2Fcreators_name%"
                f"2Feditors_name%2Flyricists_name%2Fproducers_name%3AALL%3AEQ%3A{author}%7C-%7Ceprint_status%"
                "3Aeprint_status%3AANY%3AEQ%3Aarchive%7Cmetadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow")
    elif search_type == 'site':
        exp = (f"exp=0%7C1%7C%7Carchive%7C-%7Cq%3A%3AALL%3AIN%3A{author}+{site_inst_new}%7C-%7C")
    else:
        raise ValueError('search_type must equal either "site" or "inst"') 

    # define parameters to 
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
    #submit to centaur to get id and title
    response = requests.get(request_url)
    #parse text
    references = response.text

    # parse html
    ref_html = BeautifulSoup(references, 'html.parser')
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
    # sort by year - omit non Grimmond papers (or Kent thesis)
    if search_type == 'site':
        ref_df = ref_df.sort_values('year', ascending = False)
        ref_df[ref_df['Reference'].str.contains('Grimmond') | ref_df['Reference'].str.contains('Kent')]
    #define out dir
    ref_dir = out_dir
    if os.path.exists(ref_dir) == False:
        os.makedirs(ref_dir)
    ref_file_name =  f'{site_inst}_references.csv'
    ref_file_path = os.path.join(ref_dir, ref_file_name)
    #write
    ref_df.to_csv(ref_file_path, index = False)
#%%
#loop through instruments
all_insts = inst_df['instId']
for instId in all_insts:
    get_references(base_url_inst, instId, author, 'inst', inst_out_dir)
#%%
#loop through sites 
all_sites = site_df[['id', 'network']]
for index, site in all_sites.iterrows():
    out_dir = os.path.join(site_out_dir, site['network'],'sites','references')
    get_references(base_url_site, site['id'], author, 'site', out_dir)

# %%
