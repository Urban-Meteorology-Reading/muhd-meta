requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.4414, -0.93795], 13);

var geojsonFeature = {"geometry": {"coordinates": [-0.93795, 51.4414], "type": "Point"}, "properties": {"amenity": "Site", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/URAO.html", "site_name": "URAO"}, "type": "Feature"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});