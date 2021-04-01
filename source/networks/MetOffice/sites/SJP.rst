.. _SJP:

***
SJP
***

Introduction
############

.. include:: intros/SJP_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/SJP_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/MetOffice/SJP_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/SJP_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/SJP_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/SJP/stj_met1_25843954962_o.jpg
   :width: 50 %

   Weather station at SJP 10-06-2010.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########

#. Hertwig, D., Ng, M., Grimmond, S., Vidale, P. L. and McGuire, P. C. (2021) High-resolution global climate simulations: representation of cities. International Journal of Climatology. ISSN 0899-8418 doi: https://doi.org/10.1002/joc.7018

