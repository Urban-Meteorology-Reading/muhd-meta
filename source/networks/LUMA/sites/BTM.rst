.. _BTM:

***
BTM
***

Introduction
############

.. include:: intros/BTM_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BTM_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/BTM_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BTM_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BTM_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/BTM/24502696680_1169fdd011_o.jpg
   :width: 50 %

   :ref:`SM300` node 02-02-2016.

.. figure:: photos/BTM/24502701210_8576c434ec_o.jpg
   :width: 50 %

   :ref:`SM300` node 02-02-2016.

.. figure:: photos/BTM/sort-kjell-2_23689050041_o.jpg
   :width: 50 %

   :ref:`SM300` node 02-10-2015.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/BTM_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

Acknowledgements
################

We thank Barbican and Indoor site residents for site access.

