.. _DKS:

***
DKS
***

Introduction
############

.. include:: intros/DKS_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/DKS_meta.csv
   :stub-columns: 2

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/ClearfLo/DKS_map"]);

   </script>

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/DKS_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/DKS_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/DKS_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to profiles
   :file: deployments/profile_deployments/DKS_profile_deployments.csv
   :header-rows: 2

Photos
######

Supplementary information
#########################

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########


Acknowledgements
################

