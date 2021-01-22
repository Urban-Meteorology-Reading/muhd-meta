# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:28:54 2020

@author: kitbe
"""
#%%
import os
import pandas as pd
import sqlite3
import get_reference_functions as get_ref
#%%
#author in search parameters 
author = 'Grimmond'
#base url to submit to for instruments and sites - simple search works best for sites and advanced for inst - advanced tends to find too few and simple too many
base_url_adv = 'http://centaur.reading.ac.uk/cgi/search/archive/advanced/export_reading_IDandHTML.html'
base_url_simp = "http://centaur.reading.ac.uk/cgi/search/archive/simple/export_reading_IDandHTML.html"
# out directory for instruments
inst_out_dir = os.path.join('..','source','instruments','instIds','references')
# out directory for sites
site_out_dir = os.path.join('..','source','networks')
inst_out_dir = os.path.join('..','source','instrument_types')
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
# read in omissions and additions csvs
omit_df, omit_df_exists, add_df, add_df_exists = get_ref.read_additions_omissions(os.path.join('..', 'source', 'references'))
#%%
#loop through instruments
all_insts = inst_df[['instId', 'type']]
for index, instId in all_insts.iterrows():
    print(f"getting references for {instId['instId']}")
    out_dir = os.path.join(inst_out_dir, instId['type'],'instIds','references')
    get_ref.get_references(base_url_adv, base_url_simp, instId['instId'], author, 'inst', out_dir, omit_df_exists, omit_df, add_df_exists, add_df)
#%%
# there are 2 search protocols - the specific (used for inst) and non specific (used for most sites)
# the non specific protocol should be used for these sites to prevent too many references being returned
spec_search_sites = ['MR', 'CH', 'OH', 'RH', 'GL', 'HAN', 'NK', 'TEM', 'CT']
#loop through sites 
all_sites = site_df[['id', 'network']]
for index, site in all_sites.iterrows():
    print(f"getting references for {site['id']}")
    out_dir = os.path.join(site_out_dir, site['network'],'sites','references')
    if site['id'] not in spec_search_sites:
        get_ref.get_references(base_url_adv, base_url_simp, site['id'], author, 'site', out_dir, omit_df_exists, omit_df, add_df_exists, add_df)
    # these return way too many - use more refined inst style search
    else:
        get_ref.get_references(base_url_adv, base_url_simp, site['id'], author, 'inst', out_dir, omit_df_exists, omit_df, add_df_exists, add_df)

# %%
