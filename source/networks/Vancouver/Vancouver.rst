.. _Vancouver:

*********
Vancouver
*********

.. include:: Vancouver_intro.rst

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   )};

   requirejs(["../../_static/network_maps/Vancouver_map"]);

   </script>

.. toctree::
   :caption: Vancouver sites
   :maxdepth: 1
   :glob:

   sites/*