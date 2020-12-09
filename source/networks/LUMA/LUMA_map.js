requirejs(['leaflet'], function (L) {

  var mymap = L.map('mapid').setView([51.505, -0.09], 13);
  
  var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "siteid",
        "amenity": "SITE",
        "popupContent": "A Site"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [0, 51]
    }
   };
   
   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
   }).addTo(mymap);
   
   L.geoJSON(geojsonFeature).addTo(mymap);
  
});