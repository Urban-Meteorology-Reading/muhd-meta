.. _networks:

Networks
========

The instrumentation :ref:`networks<network_def>` that contrive MUHD.

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

   paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
         'markercluster': 'Leaflet.markercluster-1.4.1/dist/leaflet.markercluster-src',   
      },
      shim: {
         leaflet: {
               exports: 'L'
         },
         markercluster: {
               deps: ['leaflet']
         }
      }
   });

   requirejs(["../_static/network_maps/all_site_map"]);

   </script>

.. toctree::
   :caption: MUHD sites
   :maxdepth: 2
   :glob:

   */*
   