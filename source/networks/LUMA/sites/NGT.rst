.. _NGT:

***
NGT
***

Site metadata
#############

.. csv-table:: 
   :file: meta/NGT_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/LUMA/NGT_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/NGT_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/NGT_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Metadata specific to scintillometers
   :file: deployments/scint_deployments/NGT_scint_deployments.csv
   :header-rows: 2

Photos
######

.. figure:: photos/NGT/img_9254_25741989922_o.jpg
   :width: 100 %

   View of tower. Unknown date between 11-10-2011 and 27-02-2013.

.. figure:: photos/NGT/grenfell_tower_las_davis_25964971515_o.jpg
   :width: 50 %

   :ref:`DAVIS`, :ref:`LAS150` reciever from :ref:`NDT` and :ref:`LASMKII` transmitter to :ref:`NTT` 11-01-2012. 

.. figure:: photos/NGT/grenfell_tower_las060030_23705912491_o.jpg
   :width: 50 %

   :ref:`LAS150` view to :ref:`NTT` 06-01-2012.

.. figure:: photos/NGT/r0015605_23705975201_o.jpg
   :width: 50 %

   :ref:`BLS` reciever and :ref:`LASMKII` unknown date between 2012-09-21 and 2013-02-26.

.. figure:: photos/NGT/img_0474_23788636795_o.jpg
   :width: 50 %

   :ref:`BLS` transmitter to :ref:`NDT` and :ref:`LAS150` reciever from :ref:`NDT` 25-05-2011.

Data acquisition
################

.. include:: ../../../data_acquisition/data_acquisition_default.rst

Data availability
#################

.. raw:: html

   <iframe src="../../../_static/availability_plots/NGT_availability.html" height="600px" width="1200px" allowfullscreen=true style="border:0px;"></iframe>
*Double click on legend to isolate instruments.*

Acknowledgements
################

We thank Adrian Bowmann at Royal Borough of Kensington and Chelsea  for site access.

