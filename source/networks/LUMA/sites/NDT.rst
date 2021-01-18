.. _NDT:

***
NDT
***

Introduction
############

.. include:: intros/NDT_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/NDT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/NDT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/NDT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/NDT_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/NDT_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to scintillometers
   :file: deployments/scint_deployments/NDT_scint_deployments.csv
   :header-rows: 2

Photos
######

.. figure:: photos/NDT/pano_20130313_141953_25232367034_o.jpg
   :width: 100 %

   Panoramic 13-03-2013.

.. figure:: photos/NDT/dartrey_tower_las_cityscan_bls_23161439553_o.jpg
   :width: 50 %

   :ref:`BLS` reciever from :ref:`NTT` and :ref:`LAS150` transmitter to :ref:`NGT` 11-01-2012. 

.. figure:: photos/NDT/dartrey-bls-view-to-trellick_23679847542_o.jpg
   :width: 50 %

   :ref:`BLS` view to :ref:`NTT` 24-05-2011.

.. figure:: photos/NDT/dartrey-bls-view-to-trellick-2_23420370559_o(1).jpg
   :width: 50 %

   :ref:`BLS` view to :ref:`NTT` 24-05-2011.

.. figure:: photos/NDT/dartrey_tower_davis_station_2_23160140304_o.jpg
   :width: 50 %

   :ref:`DAVIS` station 24-05-2011.

Supplementary information
#########################

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

References
##########


Acknowledgements
################

We thank Adrian Bowmann at Royal Borough of Kensington and Chelsea  for site access.

