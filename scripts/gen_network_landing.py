import os
#%%
# write a landing page for every network 
all_networks = os.listdir(os.path.join('..', 'source', 'networks'))
for network in all_networks:
    network_dir = os.path.join('..', 'source', 'networks', network)
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
        # here will be a map 
        network_file.write(f"**here will be a map of site positions**\n\n")
        #write the tree
        network_file.write(".. toctree::\n")
        network_file.write(f"   :caption: {network} sites\n")
        network_file.write(f"   :maxdepth: 1\n")
        network_file.write(f"   :numbered:\n")
        network_file.write(f"   :glob:\n\n")
        network_file.write("   sites/*")

# %%
