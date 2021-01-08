requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.5116, -0.1113], 13);

var geojsonFeature = {"geometry": {"coordinates": [-0.1113, 51.5116], "type": "Point"}, "properties": {"amenity": "Site", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/MT.html", "site_name": "MT"}, "type": "Feature"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});