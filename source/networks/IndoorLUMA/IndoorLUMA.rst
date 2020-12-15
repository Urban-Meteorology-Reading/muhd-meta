.. _IndoorLUMA:

**********
IndoorLUMA
**********

.. include:: IndoorLUMA_intro.rst

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../_static/network_maps/IndoorLUMA_map"]);

   </script>

.. toctree::
   :caption: IndoorLUMA sites
   :maxdepth: 1
   :glob:

   sites/*