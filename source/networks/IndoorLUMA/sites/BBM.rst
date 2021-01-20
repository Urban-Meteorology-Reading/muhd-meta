.. _BBM:

***
BBM
***

Site metadata
#############

.. csv-table:: 
   :file: meta/BBM_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/IndoorLUMA/BBM_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BBM_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BBM_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Metadata specific to indoor sensors
   :file: deployments/indoor_deployments/BBM_indoor_deployments.csv
   :header-rows: 2

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########


Acknowledgements
################

We thank Indoor site residents for site access.

