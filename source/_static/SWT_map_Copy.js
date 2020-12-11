requirejs(['jquery', 'leaflet'], function ($, L) {

    //$('body').html('Hello');
    
    function onEachFeature(feature, layer) {
      // does this feature have a property named popupContent?
      if (feature.properties && feature.properties.link && feature.properties.name) {
          layer.bindPopup("<a href='" + feature.properties.link + "'>" + feature.properties.name + "</a>");
      }
    }
  
    var mymap = L.map('mapid').setView([51.487765, -0.091059], 13);
    
    var url = 'SWT.geojson';
    //var bbTeam = L.geoJSON(null, {onEachFeature: forEachFeature, style: style});
    var bbTeam = L.geoJSON(null, {
            onEachFeature: onEachFeature,
    });
  
    // Get GeoJSON data and create features.
    $.getJSON(url, function(data) {
            bbTeam.addData(mymap);
    });
  
    bbTeam.addTo(map);
    
     
     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 18,
     }).addTo(mymap);
  
  });