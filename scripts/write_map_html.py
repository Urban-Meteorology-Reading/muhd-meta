def write_map_html(map_dir, FILE):
    # write the raw html required to display a slippy map
    FILE.write('.. raw:: html\n\n')
    FILE.write('   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>\n\n')
    FILE.write('   <script type="text/javascript">\n\n')
    FILE.write('   requirejs.config({\n\n')
    FILE.write('      paths: {\n')
    FILE.write('         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",\n')
    FILE.write('      }\n')
    FILE.write('   });\n\n')
    FILE.write(f'   requirejs(["{map_dir}"]);\n\n')
    FILE.write('   </script>\n\n')
    FILE.write('   <br />\n\n')
