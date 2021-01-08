requirejs(['leaflet'], function (L) {

function onEachFeature(feature, layer) {
    layer.bindPopup("<a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a>");
}

var mymap = L.map('mapid').setView([51.483035, -0.485565], 10);

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSK.html", "site_name": "KSK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.115968, 51.51137], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSK15S.html", "site_name": "KSK15S"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11635, 51.512], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSS.html", "site_name": "KSS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11675, 51.51178], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSS45W.html", "site_name": "KSS45W"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092951, 51.520559], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BCT.html", "site_name": "BCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.094398, 51.520532], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BFCL.html", "site_name": "BFCL"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.093295, 51.518777], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BGH.html", "site_name": "BGH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092969, 51.520551], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BCTW.html", "site_name": "BCTW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.116722, 51.511794], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSSW.html", "site_name": "KSSW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1796, 51.4814], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NDT.html", "site_name": "NDT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.106186, 51.526055], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IML.html", "site_name": "IML"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.106086, 51.526148], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IMU.html", "site_name": "IMU"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.2134, 51.521055], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NK.html", "site_name": "NK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.215762, 51.514164], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NGT.html", "site_name": "NGT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.115947, 51.512195], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSNW.html", "site_name": "KSNW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSC.html", "site_name": "KSC"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.17492, 51.501517], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RGS.html", "site_name": "RGS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.116351, 51.512104], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSB.html", "site_name": "KSB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.154566, 51.52253], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/MR.html", "site_name": "MR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.93795, 51.4414], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/URAO.html", "site_name": "URAO"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11768, 51.50975], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/TLI.html", "site_name": "TLI"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1438, 51.5139], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/HAN.html", "site_name": "HAN"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1113, 51.5116], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/MT.html", "site_name": "MT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.113, 51.5112], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/TEM.html", "site_name": "TEM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1217, 51.5081], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/EMB.html", "site_name": "EMB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.095688, 51.519515], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BTM.html", "site_name": "BTM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.937381, 51.43877], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RMR.html", "site_name": "RMR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.138843, 51.521454], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BTT.html", "site_name": "BTT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.205439, 51.523705], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NTT.html", "site_name": "NTT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.086735, 51.503546], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KGG.html", "site_name": "KGG"}, "type": "Feature"}, {"geometry": {"coordinates": [0.0, 51.51], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/GL.html", "site_name": "GL"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.091059, 51.487765], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html", "site_name": "SWT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.137242, 51.522003], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/ARUP.html", "site_name": "ARUP"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1036, 51.52667], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/WCT.html", "site_name": "WCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.104732, 51.482889], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SCT.html", "site_name": "SCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1043, 51.5273], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/CUB.html", "site_name": "CUB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.97113, 51.45625], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RAG.html", "site_name": "RAG"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.037491, 51.449684], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/HOP.html", "site_name": "HOP"}, "type": "Feature"}], "type": "FeatureCollection"};

L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
}).addTo(mymap);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}).addTo(mymap);

});