requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.5271, -0.27324], 10);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.12948, 51.5042], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice.html", "network_name": "MetOffice", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice/sites/SJP.html", "site_name": "SJP"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.417, 51.55], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice.html", "network_name": "MetOffice", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice/sites/MNH.html", "site_name": "MNH"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});