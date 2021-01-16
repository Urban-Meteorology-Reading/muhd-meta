.. _MAGIC:

*****
MAGIC
*****

.. include:: MAGIC_intro.rst

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../_static/network_maps/networks/MAGIC_map"]);

   </script>

   <br />

.. toctree::
   :caption: MAGIC sites
   :maxdepth: 1
   :glob:

   sites/*