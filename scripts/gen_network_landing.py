#%%
import os
from write_map_html import *
#%%
# write a landing page for every network 
network_dir_parent = os.path.join('..', 'source', 'networks')
all_networks = [i for i in os.listdir(network_dir_parent) if os.path.isdir(os.path.join(network_dir_parent,i))]
for network in all_networks:
    network_dir = os.path.join(network_dir_parent, network)
    network_file_name = f"{network}.rst"
    network_file = os.path.join(network_dir, network_file_name)
    with open(network_file, 'w+') as network_file:
        #write referencer
        network_file.write(f".. _{network}:\n\n")
        # write title 
        title = len(network) * '*'
        network_file.write(f"{title}\n{network}\n{title}\n\n")
        #write intro 
        network_file.write(f".. include:: {network}_intro.rst\n\n")
        # add map 
        write_map_html(f'../../_static/network_maps/{network}_map', network_file)
        #write the tree
        network_file.write(".. toctree::\n")
        network_file.write(f"   :caption: {network} sites\n")
        network_file.write(f"   :maxdepth: 1\n")
        #network_file.write(f"   :numbered:\n")
        network_file.write(f"   :glob:\n\n")
        network_file.write("   sites/*")

#%%
