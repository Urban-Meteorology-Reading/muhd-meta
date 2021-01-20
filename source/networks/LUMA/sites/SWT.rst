.. _SWT:

***
SWT
***

Introduction
############

.. include:: intros/SWT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/SWT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/SWT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/SWT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/SWT_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Metadata specific to profiles
   :file: deployments/profile_deployments/SWT_profile_deployments.csv
   :header-rows: 2

.. csv-table:: Metadata specific to scintillometers
   :file: deployments/scint_deployments/SWT_scint_deployments.csv
   :header-rows: 2

Photos
######

.. figure:: photos/SWT/27308473030_79b08b55b1_o.jpg

   View facing NNE 10-06-2016.

.. figure:: photos/SWT/27585485085_3ee6670789_o.jpg

   View facing SSW 10-06-2016.

.. figure:: photos/SWT/23-07-2020_(38).JPEG
   :width: 50 %

   View of mast, temperature and humidity sensors ( :ref:`SWTWXSTATION` ) , scintillometers and :ref:`CNR1` 23-07-2020.

.. figure:: photos/SWT/23-07-2020_(16).JPEG
   :width: 50 %

   :ref:`ARG100` and :ref:`CL31` 23-07-2020.

.. figure:: photos/SWT/19-07-2019_(12).JPG
   :width: 50 %

   Scintillometers. :ref:`LASMKII` transmitter to SCT and :ref:`BLS` reciever from IMU 19-07-2019.

Supplementary information
#########################

.. list-table:: 
   :header-rows: 1

   * - Link
     - Title
     - Description
   * - http://data.urban-climate.net/southwark_plots/
     - Southwark Meteorological Station
     - Current weather data visualisation and download 

Data acquisition
################

.. include:: data_acquisition/SWT_data_acquisition.rst

References
##########


Acknowledgements
################

We thank Bill Legassick at Southwark Council for site access.

