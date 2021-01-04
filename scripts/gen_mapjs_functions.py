def get_focus_point(network_sites):
    maxes = network_sites.max()
    mins = network_sites.min()

    max_min_dif_lat = maxes.latitude - mins.latitude
    max_min_dif_lon = maxes.longitude - mins.longitude 

    mid_point_lat = mins.latitude + (max_min_dif_lat/2)
    mid_point_lon = mins.longitude + (max_min_dif_lon/2)

    #get zoom - inferred from spread
    #if one point
    if max_min_dif_lat == 0 and max_min_dif_lon == 0:
        zoom = 13
    # city wide approx
    elif 3 >= max_min_dif_lat > 0  or 3 >= max_min_dif_lon > 0:
        zoom = 10
    # world wide
    elif max_min_dif_lat > 3 or max_min_dif_lon > 3:
        zoom = 3
    
    return mid_point_lat, mid_point_lon, zoom

def get_networks_geojson(sites_df):
    import geojson

    site_features = []
    for index, site in sites_df.iterrows():
        site_properties = {'site_name': site['id'],
                            'amenity': 'Site',
                            'site_link': f'https://muhd.readthedocs.io/en/latest/networks/{site["network"]}/sites/{site["id"]}.html',
                            'network_name': site['network'],
                            'network_link': f'https://muhd.readthedocs.io/en/latest/networks/{site["network"]}.html'}
        site_feature = geojson.Feature(geometry = geojson.Point((site['longitude'], site['latitude'])),
                                        properties= site_properties)
        site_features.append(site_feature)
    network_site_locs = geojson.FeatureCollection(site_features)
    network_geojson = geojson.dumps(network_site_locs, sort_keys=True)
    
    return network_geojson

def get_site_geojson(site, network):
    import geojson

    site_properties = {'site_name': site['id'],
                       'amenity': 'Site',
                       'site_link': f'https://muhd.readthedocs.io/en/latest/networks/{network}/sites/{site["id"]}.html'}
    site_feature = geojson.Feature(geometry = geojson.Point((site['longitude'], site['latitude'])),
                                        properties= site_properties)
    site_geojson = geojson.dumps(site_feature, sort_keys=True)
    
    return site_geojson

def write_pop_fun_cluster(FILE):
    FILE.write("function onEachFeature(feature, layer) {\n")
    # does this feature have a property named link and name?
    FILE.write("    layer.bindPopup(\"Name: <a href='\" + feature.properties.site_link + \"'>\" + feature.properties.site_name + \"</a><br>Network: <a href='\" + feature.properties.network_link + \"'>\" + feature.properties.network_name + \"</a>\");\n")
    FILE.write("layer.addTo(markers);")
    FILE.write("}\n\n")

def write_pop_fun(FILE):
    FILE.write("function onEachFeature(feature, layer) {\n")
    # does this feature have a property named link and name?
    FILE.write("    layer.bindPopup(\"<a href='\" + feature.properties.site_link + \"'>\" + feature.properties.site_name + \"</a>\");\n")
    FILE.write("}\n\n")

def write_add_geojson(FILE):
    FILE.write("L.geoJSON(geojsonFeature, {\n")
    FILE.write("onEachFeature: onEachFeature\n")
    FILE.write("}).addTo(mymap);\n\n")

def write_add_geojson_cluster(FILE):
    FILE.write("var sites = L.geoJSON(geojsonFeature, {\n")
    FILE.write("onEachFeature: onEachFeature\n")
    FILE.write("});\n\n")

def write_tiles_cluster(mid_point_lat, mid_point_lon, tile_source, tile_attribution, max_zoom, FILE):
    FILE.write(f"var tiles = L.tileLayer('{tile_source}', {{\n")
    FILE.write(f"attribution: '{tile_attribution}',\n")
    FILE.write(f"maxZoom: {max_zoom},\n")
    FILE.write(f"}}), latlng = L.latLng({mid_point_lat},{mid_point_lon});\n\n")

def write_tiles(tile_source, tile_attribution, max_zoom, FILE):
    FILE.write(f"L.tileLayer('{tile_source}', {{\n")
    FILE.write(f"attribution: '{tile_attribution}',\n")
    FILE.write(f"maxZoom: {max_zoom},\n")
    FILE.write(f"}}).addTo(mymap);\n\n")

def gen_mapjs(map_path, geojson, mid_point_lat, mid_point_lon, zoom, tile_url, tile_attributions, max_zoom):
    #write a javascript file that makes a map of provided geojson
    with open(map_path, 'w') as mapjs:
      #load required packages 
      mapjs.write("requirejs(['leaflet'], function (L) {\n\n")
      # write function that creates pop up in js 
      write_pop_fun(mapjs)
      # write map init   
      mapjs.write(f"var mymap = L.map('mapid').setView([{mid_point_lat}, {mid_point_lon}], {zoom});\n\n")
      #create a list of points in geojson format
      mapjs.write("var geojsonFeature = ")
      mapjs.write(geojson)
      mapjs.write(";\n\n")
      # write part that will add these to map
      write_add_geojson(mapjs)
      #write map tiles
      write_tiles(tile_url, tile_attributions, max_zoom, mapjs)
      #write closing brackets 
      mapjs.write("});")

def gen_cluster_mapjs(map_path, geojson, mid_point_lat, mid_point_lon, zoom, tile_url, tile_attributions, max_zoom):
    #write a javascript file of a cluster map of provided geojson
    with open(map_path, 'w') as mapjs:
      #load required packages 
      mapjs.write("requirejs(['leaflet', 'markercluster'], function (L) {\n\n")
      #write map tiles
      write_tiles_cluster(mid_point_lat, mid_point_lon, tile_url, tile_attributions, max_zoom, mapjs)
      # write function that creates pop up in js 
      write_pop_fun_cluster(mapjs)
      # write map init   
      mapjs.write(f"var mymap = L.map('mapid', {{center: latlng, zoom: {zoom}, layers: [tiles]}});\n\n")
      #create a list of points in geojson format
      mapjs.write("var geojsonFeature = ")
      mapjs.write(geojson)
      mapjs.write(";\n\n")
      # write cluster markers
      mapjs.write("var markers = L.markerClusterGroup();\n\n")
      # write part that will add these to map
      write_add_geojson_cluster(mapjs)
      mapjs.write("mymap.addLayer(markers);\n\n")
      #write closing brackets 
      mapjs.write("});")