.. _reference_guide:

***************
Reference guide
***************

This reference guide aims to help users navigate around this documentation effectively to find the required information or data.

Definitions
###########

Site
****

A singular general location (e.g. building, roof, garden) where meteorological measurement equipment is deployed.

Instrument
**********

Equipment (defined by the manufacturer and make) used to measure the enviromental conditions.

Deployment
**********

The set up and status of an instrument at a site. A new set up includes changing the position (siting, height, pitch, yaw and roll) or changing the the measurement time resolution. 
The status of an instrument involves the working condition of the instrument. For example if an instrument underwent a calibration or a fix then this would constitute a new deployment. 

Data processing workflow
########################

.. mermaid:: 
    
    graph TD
        classDef default fill:#6681d0,color:#ffff,stroke:#333,stroke-width:2px;
        linkStyle default color:#6681d0
        site[Site]
        inst[Instrument]
        deployment[[Deployment]]
        raw_data[(Raw data)]
        processing_script{{"Processing code"}}
        processed_data[(Processed data)]
        site --> deployment
        inst -->|"Additional metadata <br/> e.g. position, instrument status"| deployment
        deployment -->|Raw file name format| raw_data
        raw_data --> processing_script
        inst -->|Output definition| processing_script


Finding data for a given instrument
###################################

All instrument data can be found on Zenodo.

Raw data are stored in files, where the file naming format is specific to the instruments deployment. This can be seen in the sites' metadata page.
The raw file name given is relative to RAW/<YEAR>/<CITY>/<SITE>.

Note that raw files for different deployments can be different lengths - either daily or hourly. 

Raw data is processed by the code linked on the instruments' metadata page. Most users will not have access to the processing code repos, so to view the code will need to request access from Prof. Sue Grimmond (c.s.grimmond@reading.ac.uk).

Processed data are stored in netCDF files, within a standard file structure: data/<YEAR>/<CITY>/L<LEVEL>/<SITE>/DAY/<DAY OF YEAR>.

The file name for the instrument can be found in the *Output definitions* table on the instruments' metadata page.

Output definitions encompass the level and time resolution of a file. The different levels indicate the amount of quality assurance and quality check the data goes through. Typically, level 0 indicates no quality checking, just aggregating (where file time res > raw file time res) and then converting into netCDF format. 
The file time resolution can be either the same as the raw file time resolution of greater than it, if the data has been aggregated in time.

Each file output definition stores data from certain variables, indicated in the *Variables measured by instrument* table. Often the same variable will be stored in multiple output definitions, however certain variables will only be stored in certain files with certain output definitions.

Example 
#######

Take an example of the Lup variable, measured by the :ref:`CNR1` at :ref:`SWT` on 29/11/2020. 
From the :ref:`SWT` page it can be seen when this instrument was deployed, its positioning, the raw file resolution and sample type and also the raw file format.
The CNR1 at SWT has only been deployed once at the site, over which time data has been stored in files with the naming convention of RAD/%m/rad%Y%DOY_%H.txt, where %m, %Y, %DOY and %H represent the month, year, day of year and hour of the data within the file. 
Therefore the full path will be RAW/2020/London/SWT/RAD/11/rad2020334_%H.txt, where %H can be replaced by 01 to 24 depending on the hour.

This raw data is processed into netCDF format by the instruments' processing code.
It can be seen from the CNR1 *Output definitions* table that the CNR1 outputs two levels of data, 0 and 1, at three time resolutions, 5sec, 1min and 15min (although in this example raw time resolution is 15 minutes so only 15 minute processed data is produced).
From the *Variables measured by instrument* table it can be seen that all file output definitions contain the Lup variable, with L1 applying thresholds to the data. 
The file name format is CNR1_%SITE therefore, in this case it will be CNR1_SWT. The file name will also include information on the file time resolution and the date. 
For example to obtain 15min level 1 data the full file path is data/2020/London/L1/SWT/DAY/334/CNR1_SWT_2020334_15min.nc. 
Within this file the level 1 quality checked Lup data for 29/11/2020 can be obtained. 


