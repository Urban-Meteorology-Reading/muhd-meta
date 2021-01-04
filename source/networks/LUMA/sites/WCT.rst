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
   :stub-columns: 2

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

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/WCT_deployment_raw_files.csv
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

#. Morrison, W., Kotthaus, S. and Grimmond, S. (2020) Urban surface temperature observations from ground-based thermography: intra- and inter-facet variability. Urban Climate. ISSN 2212-0955 doi: https://doi.org/10.​1016/​j.​uclim.​2020.​100748 (In Press)
#. Morrison, W., Yin, T., Lauret, N., Guilleux, J., Kotthaus, S., Gastellu-Etchegorry, J.-P., Norford, L. and Grimmond, S. (2020) Atmospheric and emissivity corrections for ground-based thermography using 3D radiative transfer modelling. Remote Sensing of Environment, 237. 111524. ISSN 00344257 doi: https://doi.org/10.1016/j.rse.2019.111524
#. Kotthaus, S. and Grimmond, C. S. B. (2018) Atmospheric boundary layer characteristics from Ceilometer measurements part 2: application to London’s urban boundary layer. Quarterly Journal of the Royal Meteorological Society, 144 (714). pp. 1511-1524. ISSN 1477-870X doi: https://doi.org/10.1002/qj.3298

Acknowledgements
################

