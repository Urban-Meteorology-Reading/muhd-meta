.. _HOP:

***
HOP
***

Introduction
############

.. include:: intros/HOP_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/HOP_meta.csv
   :stub-columns: 2

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/LUMA/HOP_map"]);

   </script>

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/HOP_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/HOP_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/HOP_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to profiles
   :file: deployments/profile_deployments/HOP_profile_deployments.csv
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

#. Harrison, R. M., Beddows, D. C. S., Alam, M. S., Singh, A., Brean, J., Xu, R., Kotthaus, S. and Grimmond, S. (2019) Interpretation of particle number size distributions measured across an urban area during the FASTER campaign. Atmospheric Chemistry and Physics, 19 (1). pp. 39-55. ISSN 1680-7324 doi: https://doi.org/10.5194/acp-19-39-2019
#. Helfter, C., Tremper, A. H., Halios, C. H., Kotthaus, S., Bjorkegren, A., Grimmond, C. S. B., Barlow, J. F. and Nemitz, E. (2016) Spatial and temporal variability of urban fluxes of methane, carbon monoxide and carbon dioxide above London, UK. Atmospheric Chemistry and Physics, 16 (16). pp. 10543-10557. ISSN 1680-7316 doi: https://doi.org/10.5194/acp-16-10543-2016

Acknowledgements
################

