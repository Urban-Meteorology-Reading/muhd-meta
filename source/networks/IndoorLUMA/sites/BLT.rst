.. _BLT:

***
BLT
***

Introduction
############

.. include:: intros/BLT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BLT_meta.csv
   :stub-columns: 2

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   )};

   requirejs(["../../../_static/network_maps/IndoorLUMA/BLT_map"]);

   </script>

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BLT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BLT_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/BLT_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to indoor sensors
   :file: deployments/indoor_deployments/BLT_indoor_deployments.csv
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

#. Biggart, M., Stocker, J., Doherty, R. M., Wild, O., Hollaway, M., Carruthers, D., Li, J., Zhang, Q., Wu, R., Kotthaus, S., Grimmond, S., Squires, F. A., Lee, J. and Shi, Z. (2020) Street-scale air quality modelling for Beijing during a winter 2016 measurement campaign. Atmospheric Chemistry and Physics, 20 (5). pp. 2755-2780. ISSN 1680-7324 doi: https://doi.org/10.5194/acp-20-2755-2020

Acknowledgements
################

