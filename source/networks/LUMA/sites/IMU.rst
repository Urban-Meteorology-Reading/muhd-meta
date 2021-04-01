.. note::
   Check the supplementary info below for important information on the data. 

.. _IMU:

***
IMU
***

Introduction
############

.. include:: intros/IMU_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/IMU_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/IMU_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/IMU_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/IMU_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Metadata specific to profiles
   :file: deployments/profile_deployments/IMU_profile_deployments.csv
   :header-rows: 2

.. csv-table:: Metadata specific to scintillometers
   :file: deployments/scint_deployments/IMU_scint_deployments.csv
   :header-rows: 2

Photos
######

.. figure:: photos/IMU/img_2860_36022305881_o.jpg
   :width: 100 %

   Panoramic facing East 21-07-2017.

.. figure:: photos/IMU/img_2804_36154912395_o.jpg
   :width: 50 %

   View of Michael Cliffe House from :ref:`WCT` 21-07-2017.

.. figure:: photos/IMU/2016-04-18-173109_26519389685_o.jpg
   :width: 50 %

   :ref:`BLS` transmitter, :ref:`PI160`, :ref:`PAR`, :ref:`UVA`, :ref:`UVB`, :ref:`PIR`, :ref:`PSP`, :ref:`DAVIS`, :ref:`CNR1`, :ref:`CSAT3` and :ref:`LI7500A` looking West 18-04-2016.

.. figure:: photos/IMU/2013-07-25-154246_25836727066_o.jpg
   :width: 50 %

   :ref:`DAVIS` looking South West 25-07-2013.

.. figure:: photos/IMU/08-01-2020_(9).JPEG
   :width: 50 %

   :ref:`TRISONICAWS`, :ref:`DAVIS`, :ref:`CSAT3` and :ref:`LI7500A` 08-01-2020.

.. figure:: photos/IMU/img_20180530_134613767_hdr_42494980621_o.jpg
   :width: 50 %

   :ref:`CL31` looking  North East 30-05-2018.

.. figure:: photos/IMU/2014-04-10-160311_25236186713_o.jpg
   :width: 50 %

   :ref:`LASMKII` reciever from :ref:`BCT` 10-04-2014.

Supplementary information
#########################

.. list-table:: 
   :header-rows: 1

   * - Link
     - Title
     - Description
   * - :download:`IMU PSP and SPN1 radiation sensor blocking <../../../supplementary_info/imu_psp_spn1_blocking/IMU_PSP_and_SPN1_radiation_sensor_blocking.pdf>`
     - IMU PSP and SPN1 radiation sensor blocking
     - Details of suspected interference of measurements by PSP and SPN1 at IMU by telecommunications equipment.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/IMU_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

References
##########

#. Morrison, W., Kotthaus, S. and Grimmond, S. (2021) Urban surface temperature observations from ground-based thermography: intra- and inter-facet variability. Urban Climate, 35. 100748. ISSN 2212-0955 doi: https://doi.org/10.1016/j.uclim.2020.100748
#. Morrison, W., Yin, T., Lauret, N., Guilleux, J., Kotthaus, S., Gastellu-Etchegorry, J.-P., Norford, L. and Grimmond, S. (2020) Atmospheric and emissivity corrections for ground-based thermography using 3D radiative transfer modelling. Remote Sensing of Environment, 237. 111524. ISSN 00344257 doi: https://doi.org/10.1016/j.rse.2019.111524
#. Crawford, B., Grimmond, S. B., Gabey, A., Marconcini, M., Ward, H. C. and Kent, C. W. (2018) Variability of urban surface temperatures and implications for aerodynamic energy exchange in unstable conditions. Quarterly Journal of the Royal Meteorological Society, 144 (715). pp. 1719-1741. ISSN 1477-870X doi: https://doi.org/10.1002/qj.3325
#. Warren, E., Charlton-Perez, C., Kotthaus, S., Lean, H., Ballard, S., Hopkin, E. and Grimmond, S. (2018) Evaluation of forward-modelled attenuated backscatter using an urban ceilometer network in London under clear-sky conditions. Atmospheric Environment, 191. pp. 532-547. ISSN 1352-2310 doi: https://doi.org/10.1016/j.atmosenv.2018.04.045
#. Crawford, B., Grimmond, C. S. B., Ward, H. C., Morrison, W. and Kotthaus, S. (2017) Spatial and temporal patterns of surface-atmosphere energy exchange in a dense urban environment using scintillometry. Quarterly Journal of the Royal Meteorological Society, 143 (703). pp. 817-833. ISSN 1477-870X doi: https://doi.org/10.1002/qj.2967

Acknowledgements
################

We thank Borough of Islington for site access.

