.. _BCTW:

****
BCTW
****

Introduction
############

.. include:: intros/BCTW_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BCTW_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/BCTW_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BCTW_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BCTW_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/BCTW/p1050100_25236399043_o.jpg
   :width: 50 %

   View facing North West. The sites :ref:`IMU` and :ref:`BTT` are indicated.  14-11-2013.

.. figure:: photos/BCTW/20140123_140957_25562323310_o.jpg
   :width: 50 %

   View of City of London skyline looking towards the South East 23-01-2014.

.. figure:: photos/BCTW/20140123_121559_25742090382_o.jpg
   :width: 50 %

   :ref:`DAVIS` station looking towards the West 23-01-2014.

.. figure:: photos/BCTW/2014-03-10-150618_25236446123_o.jpg
   :width: 50 %

   :ref:`DAVIS` station and :ref:`LASMKII` receiver from :ref:`BTT` 10-03-2014.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/BCTW_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

Acknowledgements
################

We thank Barbican for site access.

