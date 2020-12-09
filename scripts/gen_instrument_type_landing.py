#%%
import os
import pandas as pd
import sqlite3
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in tables
instrument = pd.read_sql_query('SELECT * from instrument', connection)

#close connection
connection.close()
# %%
# write a landing page for every network 
instruments_dir_parent = os.path.join('..', 'source', 'instrument_types')
all_types = instrument['type'][instrument['type'] != '']

for itype in all_types:
    itype_dir = os.path.join(instruments_dir_parent, itype)
    if os.path.exists(itype_dir) == False:
        os.makedirs(itype_dir)
    itype_file_name = f"{itype}.rst"
    itype_file = os.path.join(itype_dir, itype_file_name)
    with open(itype_file, 'w+') as itype_file:
        #write referencer
        itype_file.write(f".. _{itype}:\n\n")
        # write title 
        title = len(itype) * '*'
        itype_file.write(f"{title}\n{itype}\n{title}\n\n")
        #write intro 
        itype_file.write(f".. include:: {itype}_intro.rst\n\n")
        #write the tree
        itype_file.write(".. toctree::\n")
        itype_file.write(f"   :caption: {itype} instrument IDs\n")
        itype_file.write(f"   :maxdepth: 1\n")
        #network_file.write(f"   :numbered:\n")
        itype_file.write(f"   :glob:\n\n")
        itype_file.write("   instIds/*")
# %%
