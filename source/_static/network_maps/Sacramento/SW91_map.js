requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.link && feature.properties.name) {
    layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
  }
}

var mymap = L.map('mapid').setView([38.502467, -121.761437], 13);

var geojsonFeature = {"geometry": {"coordinates": [-121.761437, 38.502467], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/SW91.html", "name": "SW91"}, "type": "Feature"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});