.. _BGH:

***
BGH
***

Introduction
############

.. include:: intros/BGH_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/BGH_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/BGH_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/BGH_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/BGH_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/BGH/24171371343_03edc3ffd9_o.jpg
   :width: 50 %

   :ref:`DAVIS` station looking towards the South East 02-02-2016.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/BGH_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

References
##########

#. Warren, E., Charlton-Perez, C., Kotthaus, S., Lean, H., Ballard, S., Hopkin, E. and Grimmond, S. (2018) Evaluation of forward-modelled attenuated backscatter using an urban ceilometer network in London under clear-sky conditions. Atmospheric Environment, 191. pp. 532-547. ISSN 1352-2310 doi: https://doi.org/10.1016/j.atmosenv.2018.04.045

Acknowledgements
################

We thank Barbican for site access.

