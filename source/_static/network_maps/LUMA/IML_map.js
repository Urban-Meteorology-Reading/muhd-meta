requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
  if (feature.properties && feature.properties.link && feature.properties.name) {
    layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
  }
}

var mymap = L.map('mapid').setView([51.526055, -0.106186], 13);

var geojsonFeature = {"geometry": {"coordinates": [-0.106186, 51.526055], "type": "Point"}, "properties": {"amenity": "Site", "link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IML.html", "name": "IML"}, "type": "Feature"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});