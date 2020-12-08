requirejs(['leaflet'], function (L) {

  function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.link && feature.properties.name) {
        layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
    }
  }

  var mymap = L.map('mapid').setView([51.487765, -0.091059], 13);
  
  var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "SWT",
        "amenity": "SITE",
        "link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [-0.091059, 51.487765]
    }
   };
   
   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 18,
   }).addTo(mymap);
   
   L.geoJSON(geojsonFeature, {
      onEachFeature: onEachFeature
    }).addTo(mymap);
  
});