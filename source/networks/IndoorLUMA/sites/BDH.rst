.. _BDH:

***
BDH
***

Introduction
############

.. include:: intros/BDH_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BDH_meta.csv
   :stub-columns: 2

.. raw: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   )};

   requirejs(["../../_static/network_maps/IndoorLUMA/BDH_map"]);

   </script>

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BDH_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BDH_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/BDH_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to indoor sensors
   :file: deployments/indoor_deployments/BDH_indoor_deployments.csv
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

