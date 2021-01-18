.. _OH:

**
OH
**

Introduction
############

.. include:: intros/OH_intro.rst

Site metadata
#############

.. csv-table:: 
   :file: meta/OH_meta.csv
   :stub-columns: 1

.. raw:: html

   <div id="mapid" style="height: 440px; border: 1px solid #AAA;"></div>

   <script type="text/javascript">

   requirejs.config({

      paths: {
         "leaflet": "https://unpkg.com/leaflet@1.7.1/dist/leaflet",
      }
   });

   requirejs(["../../../_static/network_maps/networks/IndoorLUMA/OH_map"]);

   </script>

   <br />

Deployments at site
###################

.. csv-table:: All site deployments
   :file: deployments/dates/OH_deployment_dates.csv
   :header-rows: 2

.. csv-table:: Position of deployments
   :file: deployments/positions/OH_deployment_positions.csv
   :header-rows: 2

.. csv-table:: Raw files of deployments
   :file: deployments/raw_files/OH_deployment_raw_files.csv
   :header-rows: 2

.. csv-table:: Metadata specific to indoor sensors
   :file: deployments/indoor_deployments/OH_indoor_deployments.csv
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

#. Squires, F. A., Nemitz, E., Langford, B., Wild, O., Drysdale, W. S., Acton, W. J. F., Fu, P., Grimmond, C. S. B., Hamilton, J. F., Hewitt, C. N., Hollaway, M., Kotthaus, S., Lee, J., Metzger, S., Pingintha-Durden, N., Shaw, M., Vaughan, A. R., Wang, X., Wu, R., Zhang, Q. and Zhang, Y. (2020) Measurements of traffic-dominated pollutant emissions in a Chinese megacity. Atmospheric Chemistry and Physics, 20 (14). pp. 8737-8761. ISSN 1680-7316 doi: https://doi.org/10.5194/acp-20-8737-2020
#. Shi, Z., Vu, T., Kotthaus, S., Harrison, R. M., Grimmond, S., Yue, S., Zhu, T., Lee, J., Han, Y., Demuzere, M., Dunmore, R. E., Ren, L., Liu, D., Wang, Y., Wild, O., Allan, J., Acton, W. J., Barlow, J., Barratt, B., Beddows, D., Bloss, W. J., Calzolai, G., Carruthers, D., Carslaw, D. C., Chan, Q., Chatzidiakou, L., Chen, Y., Crilley, L., Coe, H., Dai, T., Doherty, R., Duan, F., Fu, P., Ge, B., Ge, M., Guan, D., Hamilton, J. F., He, K., Heal, M., Heard, D., Hewitt, C. N., Hollaway, M., Hu, M., Ji, D., Jiang, X., Jones, R., Kalberer, M., Kelly, F. J., Kramer, L., Langford, B., Lin, C., Lewis, A. C., Li, J., Li, W., Liu, H., Liu, J., Loh, M., Lu, K., Lucarelli, F., Mann, G., McFiggans, G., Miller, M. R., Mills, G., Monk, P., Nemitz, E., O&amp;apos;Connor, F., Ouyang, B., Palmer, P. I., Percival, C., Popoola, O., Reeves, C., Rickard, A. R., Shao, L., Shi, G., Spracklen, D., Stevenson, D., Sun, Y., Sun, Z., Tao, S., Tong, S., Wang, Q., Wang, W., Wang, X., Wang, X., Wang, Z., Wei, L., Whalley, L., Wu, X., Wu, Z., Xie, P., Yang, F., Zhang, Q., Zhang, Y., Zhang, Y. and Zheng, M. (2019) In-depth study of air pollution sources and processes within Beijing and its surrounding region (APHH-Beijing). Atmospheric Chemistry and Physics (11). pp. 7519-7546. ISSN 1680-7316 doi: https://doi.org/10.5194/acp-19-7519-2019
#. Ching, J., Aliaga, D., Mills, G., Masson, V., See, L., Neophytou, M., Middel, A., Baklanov, A., Ren, C., Ng, E., Fung, J., Wong, M., Huang, Y., Martilli, A., Brousse, O., Stewart, I., Zhang, X., Shehata, A., Miao, S., Wang, X., Wang, W., Yamagata, Y., Duarte, D., Li, Y., Feddema, J., Bechtel, B., Hidalgo, J., Roustan, Y., Kim, Y., Simon, H., Kropp, T., Bruse, M., Lindberg, F., Grimmond, S., Demuzure, M., Chen, F., Li, C., Gonzales-Cruz, J., Bornstein, B., He, Q., Tzu-Ping, P., Hanna, A., Erell, E., Tapper, N., Mall, R.K. and Niyogi, D. (2019) Pathway using WUDAPT's Digital Synthetic City tool towards generating urban canopy parameters for multi-scale urban atmospheric modeling. Urban Climate, 28. 100459. ISSN 2212-0955 doi: https://doi.org/10.1016/j.uclim.2019.100459
#. Zazzeri, G., Lowry, D., Fisher, R. E., France, J. L., Lanoisell�, M., Grimmond, C. S. B. and Nisbet, E. G. (2017) Evaluating methane inventories by isotopic analysis in the London region. Scientific Reports, 7. 4854. ISSN 2045-2322 doi: https://doi.org/10.1038/s41598-017-04802-6
#. Onomura, S., Grimmond, C. S. B., Lindberg, F., Holmer, B. and Thorsson, S. (2015) Meteorological forcing data for urban outdoor thermal comfort models from a coupled convective boundary layer and surface energy balance scheme. Urban Climate, 11. pp. 1-23. ISSN 2212-0955 doi: https://doi.org/10.1016/j.uclim.2014.11.001
#. Young, D. T., Chapman, L., Muller, C. L., Cai, X. M. and Grimmond, C. S. B. (2014) A low-cost wireless temperature sensor: evaluation for use in environmental applications. Journal of Atmospheric and Oceanic Technology, 31 (4). pp. 938-944. ISSN 1520-0426 doi: https://doi.org/10.1175/JTECH-D-13-00217.1
#. Kotthaus, S. and Grimmond, C. S. B. (2012) Identification of micro-scale anthropogenic CO2, heat and moisture sources – processing eddy covariance fluxes for a dense urban environment. Atmospheric Environment, 57. pp. 301-316. ISSN 1352-2310 doi: https://doi.org/10.1016/j.atmosenv.2012.04.024
#. Crawford, B., Grimmond, C. S. B. and Christen, A. (2011) Five years of carbon dioxide fluxes measurements in a highly vegetated suburban area. Atmospheric Environment, 45 (4). pp. 896-905. ISSN 1352-2310 doi: https://doi.org/10.1016/j.atmosenv.2010.11.017
#. Baklanov, A., Grimmond, C. S. B., Alexander, M. and Athanassiadou, M. (2009) Meteorological and air quality models for urban areas. In: Meteorological and Air Quality Models for Urban Areas. Springer. doi: https://doi.org/10.1007/978-3-642-00298-4

Acknowledgements
################

We thank Indoor site residents for site access.

