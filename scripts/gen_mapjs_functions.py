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
    elif max_min_dif_lat > 0 or max_min_dif_lon > 0:
        zoom = 3
    
    return mid_point_lat, mid_point_lon, zoom


def get_network_geojson(network_sites, network):
    import geojson

    site_features = []
    for index, site in network_sites.iterrows():
        site_properties = {'name': site['id'],
                            'amenity': 'Site',
                            'link': f'https://muhd.readthedocs.io/en/latest/networks/{network}/sites/{site["id"]}.html'}
        site_feature = geojson.Feature(geometry = geojson.Point((site['longitude'], site['latitude'])),
                                        properties= site_properties)
        site_features.append(site_feature)
    network_site_locs = geojson.FeatureCollection(site_features)
    network_geojson = geojson.dumps(network_site_locs, sort_keys=True)
    
    return network_geojson

def get_site_geojson(site, network):
    import geojson

    site_properties = {'name': site['id'],
                       'amenity': 'Site',
                       'link': f'https://muhd.readthedocs.io/en/latest/networks/{network}/sites/{site["id"]}.html'}
    site_feature = geojson.Feature(geometry = geojson.Point((site['longitude'], site['latitude'])),
                                        properties= site_properties)
    site_geojson = geojson.dumps(site_feature, sort_keys=True)
    
    return site_geojson

def write_pop_fun(FILE):
    FILE.write("function onEachFeature(feature, layer) {\n")
    # does this feature have a property named link and name?
    FILE.write("  if (feature.properties && feature.properties.link && feature.properties.name) {\n")
    FILE.write("    layer.bindPopup(\"<a href='\" + feature.properties.link + \"'>\" + feature.properties.name + \"</a>\");\n")
    FILE.write("  }\n")
    FILE.write("}\n\n")

def write_add_geojson(FILE):
    FILE.write("L.geoJSON(geojsonFeature, {\n")
    FILE.write("onEachFeature: onEachFeature\n")
    FILE.write("}).addTo(mymap);\n\n")


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