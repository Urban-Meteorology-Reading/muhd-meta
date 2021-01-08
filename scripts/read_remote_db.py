# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:06:42 2021

@author: kitbe
"""
#%%
import sqlite3
import urllib.request
import os
import sys
#%%
#get credentials
user = sys.argv[1]
pw = sys.argv[2]

# where db is 
top_level_url = "https://data.urban-climate.net"
full_url = f"{top_level_url}/metadata/metadata.sq3"

# most recent db name from web 
current_db_name = 'current_metadata.sq3'
# name of database in repo now 
prev_db_name = 'metadata.sq3'
#%%
# extract most recent metadata database from web

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

#name of the most recent database 
# Add the username and password.
# If we knew the realm, we could use it instead of None.
password_mgr.add_password(None, top_level_url, user, pw)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open(full_url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)
# write the database to a file
db_response = urllib.request.urlopen(full_url)
with open(current_db_name,'wb') as meta_db:
    meta_db.write(db_response.read())
#connect to this new database 
current_db_connection = sqlite3.connect(current_db_name)

# remove token tables
current_db_cursor = current_db_connection.cursor()
current_db_cursor.execute('DROP TABLE userDataset')
current_db_cursor.execute('DROP TABLE userToken')
current_db_connection.commit()
#%%
# read the database currently in the repo
# command to get all tables
tableCompare = "SELECT name FROM sqlite_master WHERE type='table' order by name"
# tables in current db 
current_db_tables = current_db_cursor.execute(tableCompare).fetchall()

# connect to the old database 
if os.path.exists(prev_db_name):
    prev_db_connection = sqlite3.connect(prev_db_name)
    prev_db_cursor = prev_db_connection.cursor()
    # tables in previous db 
    prev_db_tables = prev_db_cursor.execute(tableCompare).fetchall()

    # check if database in the repo needs to be updated
    
    # assume the metadata db has not changed 
    renew_meta_db = False
    # are the tables present the same
    if current_db_tables == prev_db_tables:
        # loop through tables
        for table_name in current_db_tables:
            # is the table in the most recent database in the one in the repo 
            if table_name in prev_db_tables:
                print(table_name)
                # get the data from the table
                current_table_contents = current_db_cursor.execute(f'SELECT * from {table_name[0]}').fetchall()
                prev_table_contents = prev_db_cursor.execute(f'SELECT * from {table_name[0]}').fetchall()
                # if the table contents aren't the same then stop looping
                if current_table_contents != prev_table_contents:
                    print(f'{table_name} dont match between databases - database must be renewed')
                    renew_meta_db = True
                    break
                else:
                    print('Table matches')
    # if tables differ
    else:
        print('Tables dont match - database must be renewed')
        renew_meta_db = True
    #close con
    prev_db_connection.close()
else:
    renew_meta_db = True
#%%
# close connections
current_db_connection.close()

# renew metadatabase if necessary
if renew_meta_db == True:
    if os.path.exists(prev_db_name):
        os.remove(prev_db_name)
    os.rename(current_db_name, prev_db_name)    
else:
    os.remove(current_db_name)

# write a file deciding whether the workflow needs to be continued 
with open('renew_meta_db.txt', 'w+') as renew_meta_file:
    renew_meta_file.write(str(renew_meta_db))



