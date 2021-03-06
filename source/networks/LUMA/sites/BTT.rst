.. _BTT:

***
BTT
***

Introduction
############

.. include:: intros/BTT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BTT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/BTT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BTT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BTT_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Metadata specific to scintillometers
   :file: deployments/scint_deployments/BTT_scint_deployments.csv
   :header-rows: 2

Photos
######

.. figure:: photos/BTT/2014-03-05-105019_25232158214_o.jpg
   :width: 50 %

   :ref:`LASMKII` transmitter to :ref:`BCT`. Looking South West 05-03-2014.

.. figure:: photos/BTT/31161350610_715a3f7961_o.jpg
   :width: 50 %

   :ref:`BLS` and :ref:`LASMKII` 30-11-2016.

.. figure:: photos/BTT/bt_tower_las_23491564730_o.jpg
   :width: 50 %

   :ref:`LAS150` reciever from :ref:`KGG` 13-09-2011.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/BTT_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

References
##########

#. Crawford, B., Grimmond, C. S. B., Ward, H. C., Morrison, W. and Kotthaus, S. (2017) Spatial and temporal patterns of surface-atmosphere energy exchange in a dense urban environment using scintillometry. Quarterly Journal of the Royal Meteorological Society, 143 (703). pp. 817-833. ISSN 1477-870X doi: https://doi.org/10.1002/qj.2967

Acknowledgements
################

We thank BT tower for site access.

