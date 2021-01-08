requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.519935, -0.095334], 13);

var geojsonFeature = {"geometry": {"coordinates": [-0.095334, 51.519935], "type": "Point"}, "properties": {"amenity": "Site", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BDH.html", "site_name": "BDH"}, "type": "Feature"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});