.. _site_page_structure:

*************************
Site page structure
*************************

Pages for sites have a structure containing a selection of these headings. 
Note that not all headings are present for all sites.
The information for each heading is explained here:

Site id
#############

The title and page name is the site ID code. This is based on the location of site and/or the name of the building. For example the site id for Woosdford Tower in Southwark is :ref:`SWT`.

Introdction
***********

A short paragraph on the site and any useful information that doesn't fit into the other categories, listed below.

Site metadata
*************

Name, location and operational dates of the site. 

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Site ID
      * Shortened ID code for site.
    - * Full Name
      * Full name of the site
    - * Network
      * The observation :ref:`network <networks>` the site belongs to.
    - * Longitude 
      * Longitude of the site in decimal degrees (WGS 84 EPSG:4326).
    - * Latitude
      * Latitude of the site in decimal degrees (WGS 84 EPSG:4326). 
    - * Start date 
      * Date the site was first made operational.
    - * End date
      * Date the site was last operational. If empty then site is still in operation.
    - * Displacement height
      * Displacement height in metres. -999 indicates displacement height not given.
    - * City 
      * City the site is in. 

Deployments at site
*******************

All :ref:`deployments` (past and present) at the site. This is sub-divided into multiple tables.

Deployment dates
===============

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables below.
    - * Instrument ID
      * ID code of the instrument.
    - * Instrument serial
      * Serial number of the instrument, assigned by manufacturer.
    - * Type
      * Type of instrument, measurement taken.
    - * Deployment name
      * Name assigned to deployment
    - * Start date 
      * Date the deployment was made.
    - * End date
      * Date the deployment finished. If left blank then deployment is ongoing.

Deployment positions
====================

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables deployement dates table to find instrument id etc.
    - * Height
      * The height (in metres above sea level) of the instrument.
    - * Yaw
      * Yaw in decimal degrees.
    - * Pitch
      * Pitch in decimal degrees.
    - * Roll
      * Roll in decimal degrees.

Raw files of deployments
========================

Where the raw data measured throughout deployment is stored and the time information of this.

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables deployement dates table to find instrument id etc.
    - * Raw file name format
      * The file naming convention for raw files. %Y, %m, %d, %j, %H represent the year, month, day, day of year and hour of the measurements in the file, respectively.
    - * Raw file time resolution
      * Time resolution of the raw files. The unit should be given in the entry e.g. 60s.
    - * Sample type
      * Whether measurements in raw files are instantaneous or sample averages. 

Specific to profiles
====================

Only applies to deployments of instruments that take vertical profiles (e.g. array of thermometors on a tower or a ceilometer).

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables deployement dates table to find instrument id etc.
    - * Profile bottom
      * The height of the bottom of the profile (in metres above sea level).
    - * Profile top
      * The height of the top of the profile (in metres above sea level).
    - * Profile step
      * The size of steps of the profile (meters).

Specific to scintillometers
===========================

Only applies to deployments of scintillometers (:ref:`LASMKII` and :ref:`BLS`).

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables deployement dates table to find instrument id etc.
    - * Target distance
      * Distance (in metres) from transmitter to reciever.
    - * Target site
      * The site that it is transmitting to/ recieving from.
    - * Target height
      * The height (in meters above sea level) of the target reciever/ transmitter. 
    
Specific to indoor sensors
===========================

Only applies to deployments of indoor sensors (:ref:`MICROLITE`).

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Deployment ID
      * Used to cross-reference tables deployement dates table to find instrument id etc.
    - * Room type
      * Type of room e.g. office, living room.
    - * Building storey 
      * The storey of the room.
    - * Distance to window
      * Distance (in meters) of the nearest window.

Photos
******

Images of the site. Most of these have a date attached but where the date is not known, a date range is given.

Supplementary information
*************************

Any additional resources relating to the site.
If you are using data for a site, please pay close attention to the supplementary info, as it may contain important information on the data.

Data acquisition
****************

How to get access to data.

References
**********

These are references, extracted from the `Centaur <http://centaur.reading.ac.uk/>`_ repository. 
References are automatically harvested based on key words, and some manual additions and omissions are made. 
However, there is still potential for some references to be missed, or irrelevant references to be included.
Please bare this in mind when using this section. 
    
Acknowldegements
****************

Acknowledgements to those who have been pivotal in allowing and providing access to the site.