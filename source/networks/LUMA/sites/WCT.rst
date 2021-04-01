.. _WCT:

***
WCT
***

Introduction
############

.. include:: intros/WCT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/WCT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/WCT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/WCT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/WCT_deployment_positions.csv
   :header-rows: 2

Photos
######

.. figure:: photos/WCT/img_2808_35348442783_o.jpg
   :width: 100 %

   Panoramic facing South 21-07-2017.

.. figure:: photos/WCT/2014-04-10-161008_25236186783_o.jpg
   :width: 50 %

   Seen from :ref:`IMU` 10-04-2014.

.. figure:: photos/WCT/img_2832_35987206192_o.jpg
   :width: 50 %

   :ref:`PI160` 21-07-2017.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########

#. Morrison, W., Kotthaus, S. and Grimmond, S. (2021) Urban surface temperature observations from ground-based thermography: intra- and inter-facet variability. Urban Climate, 35. 100748. ISSN 2212-0955 doi: https://doi.org/10.1016/j.uclim.2020.100748
#. Morrison, W., Yin, T., Lauret, N., Guilleux, J., Kotthaus, S., Gastellu-Etchegorry, J.-P., Norford, L. and Grimmond, S. (2020) Atmospheric and emissivity corrections for ground-based thermography using 3D radiative transfer modelling. Remote Sensing of Environment, 237. 111524. ISSN 00344257 doi: https://doi.org/10.1016/j.rse.2019.111524

