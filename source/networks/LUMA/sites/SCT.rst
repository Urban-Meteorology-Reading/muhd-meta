.. _SCT:

***
SCT
***

Introduction
############

.. include:: intros/SCT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/SCT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/SCT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/SCT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/SCT_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/SCT/19-07-2019(12)(1).png
   :width: 50 %

   Seen from :ref:`SWT` 19-07-2019.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########


