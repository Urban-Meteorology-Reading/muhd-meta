requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([49.267, -123.1], 13);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-123.1, 49.267], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Vancouver.html", "network_name": "Vancouver", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Vancouver/sites/VL92.html", "site_name": "VL92"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});