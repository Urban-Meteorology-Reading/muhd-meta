.. _KSB:

***
KSB
***

Introduction
############

.. include:: intros/KSB_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/KSB_meta.csv
   :stub-columns: 2

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   )};

   requirejs(["../../../_static/network_maps/LUMA/KSB_map"]);

   </script>

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/KSB_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/KSB_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/KSB_deployment_raw_files.csv
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

#. Bjorkeren, A. B., Grimmond, C. S. B., Kotthaus, S. and Malamud, B. D. (2015) CO2 emission estimation in the urban environment: measurement of the CO2 storage term. Atmospheric Environment, 122. pp. 775-790. ISSN 1352-2310 doi: https://doi.org/10.1016/j.atmosenv.2015.10.012

Acknowledgements
################

