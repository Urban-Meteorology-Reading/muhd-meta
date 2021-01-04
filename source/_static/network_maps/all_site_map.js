requirejs(['leaflet', 'markercluster'], function (L) {

var tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
maxZoom: 18,
}), latlng = L.latLng(0,0);

function onEachFeature(feature, layer) {
    layer.bindPopup("Name: <a href='" + feature.properties.site_link + "'>" + feature.properties.site_name + "</a><br>Network: <a href='" + feature.properties.network_link + "'>" + feature.properties.network_name + "</a>");
layer.addTo(markers);}

var mymap = L.map('mapid', {center: latlng, zoom: 2, layers: [tiles]});

var geojsonFeature = {"features": [{"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSK.html", "site_name": "KSK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.115968, 51.51137], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSK15S.html", "site_name": "KSK15S"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11635, 51.512], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSS.html", "site_name": "KSS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11675, 51.51178], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSS45W.html", "site_name": "KSS45W"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092951, 51.520559], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BCT.html", "site_name": "BCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.094398, 51.520532], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BFCL.html", "site_name": "BFCL"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.093295, 51.518777], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BGH.html", "site_name": "BGH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092969, 51.520551], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BCTW.html", "site_name": "BCTW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.116722, 51.511794], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSSW.html", "site_name": "KSSW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1796, 51.4814], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NDT.html", "site_name": "NDT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.106186, 51.526055], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IML.html", "site_name": "IML"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.106086, 51.526148], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IMU.html", "site_name": "IMU"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.2134, 51.521055], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NK.html", "site_name": "NK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.215762, 51.514164], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NGT.html", "site_name": "NGT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.115947, 51.512195], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSNW.html", "site_name": "KSNW"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSC.html", "site_name": "KSC"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.17492, 51.501517], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RGS.html", "site_name": "RGS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.12948, 51.5042], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice.html", "network_name": "MetOffice", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice/sites/SJP.html", "site_name": "SJP"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.116351, 51.512104], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KSB.html", "site_name": "KSB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.154566, 51.52253], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/MR.html", "site_name": "MR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.93795, 51.4414], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/URAO.html", "site_name": "URAO"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096576, 51.519501], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BMH.html", "site_name": "BMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.11768, 51.50975], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/TLI.html", "site_name": "TLI"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1438, 51.5139], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/HAN.html", "site_name": "HAN"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1113, 51.5116], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/MT.html", "site_name": "MT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.113, 51.5112], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/TEM.html", "site_name": "TEM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1217, 51.5081], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/EMB.html", "site_name": "EMB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.095688, 51.519515], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BTM.html", "site_name": "BTM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.094842, 51.52027], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BST.html", "site_name": "BST"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.095334, 51.519935], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BDH.html", "site_name": "BDH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1161, 51.51146], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/KCLK.html", "site_name": "KCLK"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.111207, 51.52841], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/VH.html", "site_name": "VH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.091402, 51.519593], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BSH.html", "site_name": "BSH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.09139, 51.519043], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BBM.html", "site_name": "BBM"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.113785, 51.529834], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/OH.html", "site_name": "OH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.114697, 51.536963], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/CH.html", "site_name": "CH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097763, 51.528589], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/RH.html", "site_name": "RH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096026, 51.519016], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BTMH.html", "site_name": "BTMH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10602, 51.536287], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BH.html", "site_name": "BH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.097435, 51.526867], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/LVS.html", "site_name": "LVS"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.092698, 51.347983], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/MFR.html", "site_name": "MFR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.937381, 51.43877], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RMR.html", "site_name": "RMR"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.096744, 51.519903], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA.html", "network_name": "IndoorLUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/IndoorLUMA/sites/BLT.html", "site_name": "BLT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.138843, 51.521454], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/BTT.html", "site_name": "BTT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.205439, 51.523705], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/NTT.html", "site_name": "NTT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.086735, 51.503546], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/KGG.html", "site_name": "KGG"}, "type": "Feature"}, {"geometry": {"coordinates": [139.42, 36.01], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/TokyoIT.html", "network_name": "TokyoIT", "site_link": "https://muhd.readthedocs.io/en/latest/networks/TokyoIT/sites/CT.html", "site_name": "CT"}, "type": "Feature"}, {"geometry": {"coordinates": [0.0, 51.51], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/GL.html", "site_name": "GL"}, "type": "Feature"}, {"geometry": {"coordinates": [116.370677, 39.974506], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/IAP.html", "site_name": "IAP"}, "type": "Feature"}, {"geometry": {"coordinates": [0.582642, 51.307951], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ClearfLo.html", "network_name": "ClearfLo", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ClearfLo/sites/DKS.html", "site_name": "DKS"}, "type": "Feature"}, {"geometry": {"coordinates": [-1.396022, 50.936795], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh.html", "network_name": "ReFresh", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh/sites/SHU.html", "site_name": "SHU"}, "type": "Feature"}, {"geometry": {"coordinates": [-76.5215, 39.4128], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/BLTER.html", "network_name": "BLTER", "site_link": "https://muhd.readthedocs.io/en/latest/networks/BLTER/sites/BCH.html", "site_name": "BCH"}, "type": "Feature"}, {"geometry": {"coordinates": [-121.325076, 38.630489], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento.html", "network_name": "Sacramento", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/CSU.html", "site_name": "CSU"}, "type": "Feature"}, {"geometry": {"coordinates": [-121.761437, 38.502467], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento.html", "network_name": "Sacramento", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/SW91.html", "site_name": "SW91"}, "type": "Feature"}, {"geometry": {"coordinates": [-121.064065, 38.591214], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento.html", "network_name": "Sacramento", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Sacramento/sites/SD91.html", "site_name": "SD91"}, "type": "Feature"}, {"geometry": {"coordinates": [-99.13, 19.43], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MexicoCity.html", "network_name": "MexicoCity", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MexicoCity/sites/ME93.html", "site_name": "ME93"}, "type": "Feature"}, {"geometry": {"coordinates": [-123.1, 49.267], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Vancouver.html", "network_name": "Vancouver", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Vancouver/sites/VL92.html", "site_name": "VL92"}, "type": "Feature"}, {"geometry": {"coordinates": [-87.8, 41.95], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/Chicago.html", "network_name": "Chicago", "site_link": "https://muhd.readthedocs.io/en/latest/networks/Chicago/sites/C95U.html", "site_name": "C95U"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.091059, 51.487765], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html", "site_name": "SWT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.137242, 51.522003], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/ARUP.html", "site_name": "ARUP"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1036, 51.52667], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/WCT.html", "site_name": "WCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.104732, 51.482889], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SCT.html", "site_name": "SCT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10475, 51.4987], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MAGIC AirPro.html", "network_name": "MAGIC AirPro", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MAGIC AirPro/sites/MAGIC_WT.html", "site_name": "MAGIC_WT"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.1043, 51.5273], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/CUB.html", "site_name": "CUB"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.417, 51.55], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice.html", "network_name": "MetOffice", "site_link": "https://muhd.readthedocs.io/en/latest/networks/MetOffice/sites/MNH.html", "site_name": "MNH"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.97113, 51.45625], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/RAG.html", "site_name": "RAG"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.10201, 51.498149], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh.html", "network_name": "ReFresh", "site_link": "https://muhd.readthedocs.io/en/latest/networks/ReFresh/sites/SBU.html", "site_name": "SBU"}, "type": "Feature"}, {"geometry": {"coordinates": [-0.037491, 51.449684], "type": "Point"}, "properties": {"amenity": "Site", "network_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA.html", "network_name": "LUMA", "site_link": "https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/HOP.html", "site_name": "HOP"}, "type": "Feature"}], "type": "FeatureCollection"};

var markers = L.markerClusterGroup();

var sites = L.geoJSON(geojsonFeature, {
onEachFeature: onEachFeature
});

mymap.addLayer(markers);

});