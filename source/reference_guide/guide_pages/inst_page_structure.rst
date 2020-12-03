.. _inst_page_structure:

*************************
Instrument page structure
*************************

All pages for instruments follow a standard page structure. This structure is explained here:

Instrument id
#############

The title and page name is the instrument ID code. This is often the model of the instrument (e.g. :ref:`CL31`) but sometimes is less generic (e.g. :ref:`SWTWXSTATION`).

Introdction
***********

A short paragraph on what the instrument is and any useful information that doesn't fit into the other categories, listed below.

Manufacturer and Model
**********************

The company that manufactures the instrument and the model and type of the instrument.

Output definitions
******************

Processed data from instruments is stored in netCDF files. An instrument can have multiple netCDF files for the same time frame due to having multiple output definitions.
The output definition defines the name of the output file, the number of levels of data and the time resolution(s) of the output data.  

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Output definition ID
      * Used to identify the output definition in the "Variables measured by instrument" table.
    - * File Identifier
      * The standard prefix file format to which processed data is saved %SITE and %LETTER are replaced by the instruments' site and suffix, respectively. 
    - * Level Number
      * The code for the processing level of data. Higher levels are processed and quality checked more rigorously.
    - * QAQC notes 
      * Quality assurance and quality control notes on this level for this output definition. Notes are non-exhaustive. To see what all each level means in more detail, see the processing code.
    - * File time resolution
      * The time resolution(s) that processed data is outputted to. 

Processing code
***************

A link to the github repo from which the code used to process data is stored. Most users will not have access to the repos so it will have to be requested from Prof. Sue Grimmond (c.s.grimmond@reading.ac.uk).

Variables measured by instrument
********************************

What the instrument measures. These variables are stored in one or more of the files' definted in the output definitions table.

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Variable ID
      * The id code for the variable. This is the name used in the netCDF file.
    - * Full Name
      * The full name of the variable
    - * Unit
      * Unit of variable.
    - * Lower threshold 
      * Lowest value the variable can be once the threshold is applied. The level at which this threshold is applied will be indicated in the "QAQC" notes column of the "Output definitions" table. Values below this threshold are replaced.
    - * Upper threshold 
      * Highest value the variable can be once the threshold is applied. The level at which this threshold is applied will be indicated in the "QAQC" notes column of the "Output definitions" table. Values below this threshold are replaced.
    - * Files present
      * In which files the variable is present for this instrument. The output ID, level and time resolution are comma separated. Where the variable is stored within multiple files, these definitions are space separated.

Serials
*******

The serial number(s) of the instruments used in the mudh database for this instrument make. 

.. list-table::
    :header-rows: 1

    - * Header
      * Explanation
    - * Serial
      * Serial number assigned by manufacturer.
    - * Suffix
      * Letter assigned to the instrument with this serial number. This is used to identify the output files for some instruments %LETTER in the "File identifier" (seen in the "Output definitions" table).
  
Deployments
***********

Where and when each individual instrument has been deployed. Note that an instrument can be deployed at the same site twice in a row if the configuration or instrument status changes (see :ref:`definitions`). 

Photos
******

Images of the instruments whilst they're deployed. Most of these have a date attached but where the date is not known, a date range is given.

Supplementary information
*************************

This includes (but is not limited to) instrument manuals. In most cases a download link is given but when this is not permissible a url link is given. If you find an expired url please contact Prof. Sue Grimmond (c.s.grimmond@reading.ac.uk).

Data acquisition
****************

How to get access to data.

References
**********

These are references, extracted from the `Centaur <http://centaur.reading.ac.uk/>`_ repository. 
References are automatically harvested based on key words, and some manual additions and omissions are made. 
However, there is still potential for some references to be missed, or irrelevant references to be included.
Please bare this in mind when using this section. 