requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.link && feature.properties.name) {
    layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
  }
}

var mymap = L.map('mapid').setView([38.566478000000004, -121.412751], 10);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-121.325076, 38.630489], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/CSU.html", "name": "CSU"}, "type": "Feature"}, {"geometry": {"coordinates": [-121.761437, 38.502467], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/SW91.html", "name": "SW91"}, "type": "Feature"}, {"geometry": {"coordinates": [-121.064065, 38.591214], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/SD91.html", "name": "SD91"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});