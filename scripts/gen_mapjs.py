#%%
import os
import sqlite3
import pandas as pd
import gen_mapjs_functions as gen_mapjs
#%%
# get connection to database
db_path = os.path.join("..", "metadata", "metadata.sq3")
connection = sqlite3.connect(db_path)

# read in site table
site_df = pd.read_sql_query('SELECT * from site', connection)

#close connection
connection.close()
#%%
# tiles to use and copyright info
tile_url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
tile_attributions = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
max_zoom = 18

# where to save map javascript files
map_dir = os.path.join('..', 'source', '_static', 'network_maps')
if os.path.exists(map_dir) == False:
      os.makedirs(map_dir)
#write javascript for all sites as a cluster map
all_site_geojson = gen_mapjs.get_networks_geojson(site_df) 
all_site_map_path = os.path.join(map_dir,"all_site_map.js")
gen_mapjs.gen_cluster_mapjs(all_site_map_path, all_site_geojson, 0, 0, 2,
                      tile_url, tile_attributions, max_zoom)
#write javascript for each site and network individually 
all_networks = site_df['network'].unique()
for network in all_networks:
  network_sites = site_df[site_df['network'] == network]
  # get map focus inferred by site locations
  mid_point_lat, mid_point_lon, zoom = gen_mapjs.get_focus_point(network_sites)
  network_geojson = gen_mapjs.get_networks_geojson(network_sites)
  #generate network map
  map_path = os.path.join(map_dir, 'networks', f"{network}_map.js")
  if os.path.exists(os.path.join(map_dir, 'networks')) == False:
      os.makedirs(os.path.join(map_dir, 'networks'))
  gen_mapjs.gen_mapjs(map_path, network_geojson, mid_point_lat, mid_point_lon, zoom,
                      tile_url, tile_attributions, max_zoom)
  # write a map for every site 
  for index, site in network_sites.iterrows():
    site_geojson = gen_mapjs.get_site_geojson(site, network)
    site_map_dir = os.path.join(map_dir, 'networks', network)
    if os.path.exists(site_map_dir) == False:
      os.makedirs(site_map_dir)
    site_map_path = os.path.join(site_map_dir, f"{site['id']}_map.js")
    gen_mapjs.gen_mapjs(site_map_path, site_geojson, site['latitude'], site['longitude'], 13,
                      tile_url, tile_attributions, max_zoom)


# %%
