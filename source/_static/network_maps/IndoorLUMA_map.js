requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.link && feature.properties.name) {
    layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
  }
}

var mymap = L.map('mapid').setView([51.442473, -0.103745], 3);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.096576, 51.519501], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BMH.html", "name": "BMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.094842, 51.52027], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BST.html", "name": "BST"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.095334, 51.519935], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BDH.html", "name": "BDH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/KCLK.html", "name": "KCLK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.111207, 51.52841], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/VH.html", "name": "VH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.091402, 51.519593], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BSH.html", "name": "BSH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.09139, 51.519043], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BBM.html", "name": "BBM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.113785, 51.529834], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/OH.html", "name": "OH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.114697, 51.536963], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/CH.html", "name": "CH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097763, 51.528589], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/RH.html", "name": "RH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096026, 51.519016], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BTMH.html", "name": "BTMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10602, 51.536287], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BH.html", "name": "BH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097435, 51.526867], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/LVS.html", "name": "LVS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092698, 51.347983], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/MFR.html", "name": "MFR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096744, 51.519903], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BLT.html", "name": "BLT"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});