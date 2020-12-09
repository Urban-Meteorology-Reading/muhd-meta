.. _LUMA:

****
LUMA
****

.. include:: LUMA_intro.rst

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script>

   requirejs.config({
   // define paths to where all of our dependencies live
   paths: {
      'leaflet': 'https://unpkg.com/leaflet@1.7.1/dist/leaflet',
   }
   });

   // require all dependencies, we still need to require our leaflet-heat and leaflet-markercluster modules so they load
   requirejs(['LUMA_map']);

   </script>


.. toctree::
   :caption: LUMA sites
   :maxdepth: 1
   :glob:

   sites/*