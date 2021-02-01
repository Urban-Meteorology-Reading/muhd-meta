.. _HAN:

***
HAN
***

Introduction
############

.. include:: intros/HAN_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/HAN_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/HAN_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/HAN_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/HAN_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/HAN/dsc05885_23761302336_o.jpg
   :width: 50 %

   Location of :ref:`SM300` (darker patch of soil) 08-06-2011.

.. figure:: photos/HAN/dscf3438_23704877001_o.jpg
   :width: 50 %

   :ref:`SM300` unnearthed 08-06-2011.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/HAN_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

