.. _TLI:

***
TLI
***

Introduction
############

.. include:: intros/TLI_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/TLI_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/TLI_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/TLI_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/TLI_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/TLI/sort-kjell_23144423273_o.jpg
   :width: 50 %

   Gangway from which water temperature sensors are deployed 03-11-2015.

.. figure:: photos/TLI/water_tinytag_1_23680520982_o.jpg
   :width: 50 %

   Pole on which :ref:`TINYTAG` were deployed 27-04-2011.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########


