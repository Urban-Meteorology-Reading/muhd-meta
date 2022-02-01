.. _SHU:

***
SHU
***

Introduction
############

.. include:: intros/SHU_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/SHU_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/ReFresh/SHU_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/SHU_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/SHU_deployment_positions.csv
   :header-rows: 2

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########

#. Hu, Y., Tan, J., Grimmond, S., Ao, X., Yan, Y. and Liu, D. (2021) Observed and modeled urban heat island and sea breeze circulation interactions: a Shanghai case study. Journal of Applied Meteorology and Climatology. ISSN 1558-8432 doi: https://doi.org/10.1175/JAMC-D-20-0246.1 (In Press)

