requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.4987, -0.10475], 13);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.10475, 51.4987], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MAGIC AirPro.html", "network_name": "MAGIC AirPro", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MAGIC AirPro/sites/MAGIC_WT.html", "site_name": "MAGIC_WT"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});