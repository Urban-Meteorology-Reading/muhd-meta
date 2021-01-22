# muhd-meta
meta-data repo for MUHD (Multi-City Urban Hydrometeorology Database)

## How to make edits

Site and instrument pages are created automatically based on the LUMA database. Please **Do not edit site or instrument pages directly** as these changes will get overwritten. To make changes to these pages please follow the guidance below.

### Introductions

The introduction is the opening for the page. Use this for a small explanation of what the site or instrument is and any additional information that does not fit elsewhere in the page.

This intro is sourced from `source/networks/NETWORKNAME/sites/intros/SITEID_intro.rst` for site pages and `source/instrument_types/INSTRUMENTTYPE/instIds/intros/INSTID_intro.rst` for instrument pages. Create/alter these files to generate/edit an intro. 

E.g. to edit [SWT intro](https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html#introduction), make your changes to [this file](source/networks/LUMA/sites/intros/SWT_intro.rst).

### Processing code 

This is a link to a github repo. Only people with access to the repo will be able to see it. People can be granted read access to the repo on request.

The links are defined in [this csv](source/supplementary_info/github_links/github_links.csv). **Inst ID** should be as it appears on the page e.g. DAVIS for a Davis Vantage Pro.

### Photos 

Adding a photos requires two things: the photos themselves and a reference csv that the program uses to put them on the page, scale it and add a caption.

Photos and the reference csv must go in the `source/networks/NETWORKNAME/sites/photos/SITEID` directory for site pages and `source/instrument_types/INSTRUMENTTYPE/instIds/photos/INSTID` directory for instrument pages. 

Import photos into this directory. Also create a csv file called `photo_ref.csv`. The csv must be formatted like this:

| name | caption | scale |
| ---- | ------- | ----- |
| Name of the image within the **photos** directory. | Caption that's added below the image. | The scale of the image (in percent). I have found 50 works okay for most images. Wide images (such as panoramics) are better at 100. |  

A row must be added for each image you want to be on the page.

For example the [photos for SWT](https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html#photos) are generated from the files in [this directory](source/networks/LUMA/sites/photos/SWT).

### Supplementary info 

Supplementary info is any other file or webpage that is relevant to the instrument or site. This includes instrument manuals.

The info is defined in [this csv file](source/supplementary_info/supplementary_info.csv). The file is formatted like this:

| Site | Inst Id | Internal | Make public | Link | Title | Description | 
| ---- | ------- | -------- | ----------- | ---- | ----- | ----------- |
| Site ID e.g. SWT. Leave blank if this is for an instrument only. | Instrument ID e.g. CSAT3. Leave blank if this is for an site only. | TRUE or FALSE. Is this a link to a file in the repo (TRUE, in this case a download link is presented) or on the internet (FALSE). | TRUE or FALSE. If TRUE the link will be added to the page, if FALSE it won't | The path or URL for the info. This can be relative to the page it will be on (defined in Site or Inst Id). E.g. the path to the CSAT3 manual (source/instrument_types/3D Sonic Anemometer/instIds/manuals/CSAT3_manual.pdf) relative to the CSAT page (source/instrument_types/3D Sonic Anemometer/instIds/CSAT3.rst) is manuals/CSAT3_manual.pdf. | How the supplementary info is named. | A short description of the contents. |

### Data acquisition 

If there is a specific method of obtaining data for a site or instrument then this should be explained in `source/networks/NETWORKNAME/sites/data_acquisition/SITEID_data_acquisition.rst` directory for site pages and `source/instrument_types/INSTRUMENTTYPE/instIds/data_acquisition/INSTID_data_acquisition.rst`.


For example, [SWT data acquisition message](https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html#data-acquisition) is defined in [this](source/networks/LUMA/sites/data_acquisition/SWT_data_acquisition.rst) file.

If this page isn't created then a [default message](source/data_acquisition/data_acquisition_default.rst) is added.

### Acknowledgements 

Acknowledgements are defined in the [site_acknowledgements csv](source/acknowledgements/site_acknowledgements.csv). Multiple sites can be used for one 'acknowledgement' by separating the site ids with a comma. This is put into a sentence for the relevant page. E.g. for [SWT](https://muhd.readthedocs.io/en/latest/networks/LUMA/sites/SWT.html#acknowledgements). 

This file, and the other csv files in the `source/acknowledgements` directory, are used for the [acknowledgements page](https://muhd.readthedocs.io/en/latest/acknowledgements/acknowledgements.html).

### References 

References are scraped automatically from [Centaur](http://centaur.reading.ac.uk/). However, this method doesn't always return the all the relevant references and sometimes returns references that aren't relevant. Therefore, it is possible to add or omit references for a given page manually. 

#### To manually add references to a page

Add the reference to the [reference_additions.csv file](source/references/reference_additions.csv). The file is formatted like this:

| Centaur ID | Full reference | Year | Page name |
| ---------- | -------------- | ---- | --------- |
| This is probably the easiest way to add a reference that is consistently formatted. It is optional if *Full reference* and *Year* is defined. The (probably) easiest way to get the Centaur ID is to search for the item on Centaur then select *HTML Citations (with IDs)* from the drop lower down menu. Then click *Export*. The Centaur ID (a number) will be next to the reference. | If the item is not on Centaur, or this is easier, then a full reference can be supplied. Please format this in the same way the automatic references are formatted. For this to be used the *Year* must also be given. | If the *Full reference* is to be used then the year the item was published must be given. Without this the reference will be ignored. | The name of the site or instrument page to add reference to, e.g. SWT or CSAT3. |

#### To manually omit references from a page

If an irrelevant reference has been found then it can be omitted using the [reference_omissions.csv file](source/references/reference_omissions.csv). The file is formatted like this:

| Centaur ID | Page name |
| ---------- | --------- |
| The (probably) easiest way to get the Centaur ID is to search for the item on Centaur then select *HTML Citations (with IDs)* from the drop lower down menu. Then click *Export*. The Centaur ID (a number) will be next to the reference. This is the most robust method of making sure the right reference is omitted | The name of the site or instrument page to add reference to, e.g. SWT or CSAT3. |

