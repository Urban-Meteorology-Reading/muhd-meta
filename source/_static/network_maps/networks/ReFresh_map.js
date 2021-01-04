requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.217472, -0.749016], 10);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-1.396022, 50.936795], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh.html", "network_name": "ReFresh", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh/sites/SHU.html", "site_name": "SHU"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10201, 51.498149], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh.html", "network_name": "ReFresh", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh/sites/SBU.html", "site_name": "SBU"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});