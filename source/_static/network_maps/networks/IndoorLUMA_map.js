requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.442473, -0.103745], 10);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.096576, 51.519501], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BMH.html", "site_name": "BMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.094842, 51.52027], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BST.html", "site_name": "BST"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.095334, 51.519935], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BDH.html", "site_name": "BDH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/KCLK.html", "site_name": "KCLK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.111207, 51.52841], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/VH.html", "site_name": "VH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.091402, 51.519593], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BSH.html", "site_name": "BSH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.09139, 51.519043], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BBM.html", "site_name": "BBM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.113785, 51.529834], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/OH.html", "site_name": "OH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.114697, 51.536963], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/CH.html", "site_name": "CH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097763, 51.528589], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/RH.html", "site_name": "RH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096026, 51.519016], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BTMH.html", "site_name": "BTMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10602, 51.536287], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BH.html", "site_name": "BH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097435, 51.526867], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/LVS.html", "site_name": "LVS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092698, 51.347983], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/MFR.html", "site_name": "MFR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096744, 51.519903], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BLT.html", "site_name": "BLT"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});