requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.307951, 0.582642], 13);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [0.582642, 51.307951], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ClearfLo.html", "network_name": "ClearfLo", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ClearfLo/sites/DKS.html", "site_name": "DKS"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});