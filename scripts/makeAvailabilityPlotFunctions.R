getLUMAsiteIDs <- function(){
  # make request to api for all sites
  url <- "https://data.urban-climate.net/metadata/queries/getSites.php"
  credentials = strsplit(readLines('credentials.txt'), ' ')[[1]]
  return <- GET(url, authenticate(credentials[1], credentials[2]))
  #extract LUMA
  allSites <- fromJSON(content(return, "text"))
  LUMAsites <- lapply(allSites, function(x){if(x[['network']] == "LUMA"){return(x)}}) %>%
    compact()
  #return site IDs
  LUMAsiteIDs <- names(LUMAsites)
  
  return(LUMAsiteIDs)
}

copyMetaDataDb <- function(serverUser, serverHost){
  #copy the metadata database to a given directory
  copyDBProc <- process$new('rsync', c(paste0(serverUser, '@', serverHost, ':/var/www/html/metadata/metadata.sq3'), 
                                       '.'), stdout = '|', stderr = '|') 
  copyDBProc$wait()
  #check it has worked
  exitStatus <- copyDBProc$get_exit_status()
  if(exitStatus != 0 ){
    stop(paste('Error copying metadata database with message:',
               copyDBProc$read_all_error()))
  }
}

getAllInstInfo <- function(){
  #copy metadata db
  copyMetaDataDb('micromet', 'data.urban-climate.net')
  
  #get tables
  dataBaseCon <- DBI::dbConnect(RSQLite::SQLite(),dbname = "metadata.sq3")
  
  position <- dbReadTable(dataBaseCon, 'position')
  position <- position %>% dplyr::select(c('deploymentId', 'instSerial'))
  
  deployment <- dbReadTable(dataBaseCon, 'deployment')
  deployment <- deployment %>% dplyr::select(c('id', 'siteId', 'startDate', 'endDate'))
  
  instSerial <- dbReadTable(dataBaseCon, 'instSerial')
  instSerial <- instSerial %>% dplyr::select(-suffix)
  
  #diconnect and delete database copy
  dbDisconnect(dataBaseCon)
  rmvDB <- file.remove('metadata.sq3')
  
  #join tables
  poitionDeployment <- merge(position, deployment, by.x = 'deploymentId', by.y = 'id')
  allInstInfo <- merge(poitionDeployment, instSerial, by.x = 'instSerial', by.y = 'serial')
  
  return(allInstInfo)
}

getEndDate <- function(endD){
  #convert NA to todays date
  if(NA %in% endD){
    return(Sys.Date())
  } else {
    return(max(endD))
  }
}

getSiteInf <- function(siteId){
  
  #get instrument info from metadata database
  allInstInfo <- getAllInstInfo()
  
  # convert to class dates
  allInstInfo <- allInstInfo %>% dplyr::mutate(startDate = as.Date(startDate)) %>% 
    dplyr::mutate(endDate = as.Date(endDate))
  
  #group by site 
  allInstInfoGrouped <- allInstInfo %>% dplyr::group_by(siteId) 
  
  siteNames <- allInstInfoGrouped %>% dplyr::group_keys()
  
  if (siteId %in% siteNames[['siteId']]){
    allInstInfoList <- allInstInfoGrouped %>% group_split() %>% 
      setNames(siteNames[['siteId']])
    
    # select info for site
    site <- allInstInfoList[[siteId]]
    # if enddate is NA then change it to todays date
    siteInf <- site %>% group_by(instSerial) %>% 
      summarise(sd = min(startDate), ed = getEndDate(endDate), instId = unique(instId)) %>%
      filter(!(instId %in% c('UVB', 'PAR')))
    } else {
      siteInf <- NULL
    }
  
  return(siteInf)
}

manSiteInfChange <- function(siteInf, siteId){
  # for sites with lots of instruments (e.g. KSSW) where instruments have been chopped 
  # and changed its easiest to do this manually sometimes
  
  
  
  return(siteInf)
}

getInstVar <- function(){
  # dataframe giving variable, level and file time resolution
  instInf <- data.frame(rbind(c('CSAT3', 'u', 0, '30min'),
                   c('GILL121R03', 'u', 0, '30min'),
                   c('CNR1', 'Kdn', 0, '15min'),
                   c('CNR4', 'Kdn', 0, '15min'),
                   c('LASMKII', 'Cn2', 0, '30min'),
                   c('BLS', 'Cn2', 0, '30min'),
                   c('SWTWXSTATION', 'Tair', 0, '15min'),
                   c('PIR', 'Ldn', 0, '15min'),
                   c('PSP', 'Kdn', 0, '15min'),
                   c('UVA', 'PAR_W', 0, '15min'),
                   c('LI7500A', 'C_CO2', 0, '30min'),
                   c('KH20', 'C_CO2', 0, '30min'),
                   c('DAVIS', 'Tair', 0, '30min'),
                   c('WXT510', 'Tair', 0, '30min'),
                   c('SPN1', 'Kdn', 0, '15min'),
                   c('CL31', 'clear', 1, '15min'),
                   c('CT25K', 'clear', 1, '15min'),
                   c('TRISONICAWS', 'Tair', 0, '15min'),
                   c('MICROLITE', 'Tair_indoor', 0, '15min'),
                   c('SM300', 'Soil_Temp', 0, '15min'),
                   c('TT200', 'Soil_Temp', 0, '15min'),
                   c('ARG100', 'rain_acc', 0, '15min'),
                   c('THERMOCOUPLE', 'Tair', 0, '30min'),
                   c('DS18B20', 'Twater', 0, '15min')), stringsAsFactors = F)
  names(instInf) <- c('instId', 'variables', 'level', 'fileTimeRes')
  return(instInf)
}

getInstData <- function(inst, instVars){
  # join variable
  instAll <- instVars %>% dplyr::filter(instId == inst[['instId']]) %>%
    dplyr::left_join(inst, by = c('instId'))
  # get the data from files
  print(instAll[['instId']])
  if ( instAll[['instId']] != 'THERMOCOUPLE'){
    instData <- analysisToolsLUMA::getLUMAdata(list(id = instAll[['instId']], site = siteId, 
                                                    serial = instAll[['instSerial']]),
                                               instAll[['level']], instAll[['sd']], instAll[['ed']], 
                                               instAll[['variables']],
                                               instAll[['fileTimeRes']])
  } else {
    instData <- analysisToolsLUMA::getLUMAdata(list(id = instAll[['instId']], site = siteId, 
                                                    serial = instAll[['instSerial']], outdef = 'Omega_T'),
                                               instAll[['level']], instAll[['sd']], instAll[['ed']], 
                                               instAll[['variables']],
                                               instAll[['fileTimeRes']])
  }
  
  return(instData)
}

manualInfoChange <- function(siteId, siteData, siteInf){
  #general ways of maniplating metadata to make it behave 
  
  #multiple SM300 at RGS - use depth in inst id
  if( siteId == 'RGS' ){
    siteInf <- siteInf %>% mutate(instId = case_when(
      instSerial %in% c('A01357', 'A01365') ~ 'SM300 -10cm',
      instSerial %in% c('A01360', 'A01366', 'A01362') ~ 'SM300 -15cm',
      TRUE ~ instId
    ))
    
    siteData <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$serial %in% c('A01357', 'A01365')){
        x$metadata$instrument$id <- 'SM300 -10cm'
      } else if (x$metadata$instrument$serial %in% c('A01360', 'A01366', 'A01362')) {
        x$metadata$instrument$id <- 'SM300 -15cm'
      }
      return(x)})
  }
  
  #KSSW the WXT and CNR4 were repleced by other instruments then returned 
  if (siteId == 'KSSW'){
    #WXT had 2 insts - one replaced the other then the first returned so program thought was 2 insts
    WXTfilt <- siteInf %>% filter(instId == 'WXT510')
    WXTnewRow <- WXTfilt %>% group_by(instId) %>%
      summarise(instSerial = paste(instSerial, collapse = '|'), sd = min(sd), 
                ed = max(ed))
    
    WXTsiteData <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$id == 'WXT510'){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
    WXTsiteDataD <- bind_rows(WXTsiteData[[1]]$data, WXTsiteData[[2]]$data)
    WXTsiteDataM <- WXTsiteData[[1]]$metadata
    WXTsiteDataM$instrument$serial <- paste(WXTsiteData[[1]]$metadata$instrument$serial,
                                            WXTsiteData[[2]]$metadata$instrument$serial,
                                            sep = '|')
    WXTsiteDataNew <- list(data = WXTsiteDataD, metadata = WXTsiteDataM)
    
    # similarly for CNR4 
    CNR4filt <- siteInf %>% filter(instId == 'CNR4')
    CNR4newRow <- CNR4filt %>% group_by(instId) %>%
      summarise(instSerial = paste(instSerial, collapse = '|'), sd = min(sd), 
                ed = max(ed))
    
    CNR4siteData <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$id == 'CNR4'){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
    CNR4siteDataD <- bind_rows(CNR4siteData[[1]]$data, CNR4siteData[[2]]$data)
    CNR4siteDataM <- CNR4siteData[[1]]$metadata
    CNR4siteDataM$instrument$serial <- paste(CNR4siteData[[1]]$metadata$instrument$serial,
                                            CNR4siteData[[2]]$metadata$instrument$serial,
                                            sep = '|')
    CNR4siteDataNew <- list(data = CNR4siteDataD, metadata = CNR4siteDataM)
    
    # replace old entries with new
    siteInf <- siteInf %>% dplyr::filter(!(instId %in% c('WXT510', 'CNR4'))) %>%
      bind_rows(CNR4newRow, WXTnewRow)
    
    #get only first Tair from temp profile
    THERMOCOUPLEsiteDataNew <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$id == 'THERMOCOUPLE'){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
    
    THERMOCOUPLEsiteDataNew[[1]]$data <- THERMOCOUPLEsiteDataNew[[1]]$data %>% 
      dplyr::select(TIME, Tair_1) %>% 
      rename(Tair = Tair_1)
    
    
    siteDataNew <- siteData %>% lapply(., function(x){
      if (!(x$metadata$instrument$id %in% c('CNR4', 'WXT510', 'THERMOCOUPLE'))){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
      
    siteDataNew[[length(siteDataNew) +1]] <-  WXTsiteDataNew
    siteDataNew[[length(siteDataNew) +1]] <-  CNR4siteDataNew
    siteDataNew[[length(siteDataNew) +1]] <-  THERMOCOUPLEsiteDataNew[[1]]
      
    siteData <- siteDataNew
  }
  
  if (siteId == 'KSS'){
    #get only first Tair from temp profile
    THERMOCOUPLEsiteDataNew <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$id == 'THERMOCOUPLE'){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
    
    THERMOCOUPLEsiteDataNew[[1]]$data <- THERMOCOUPLEsiteDataNew[[1]]$data %>% 
      dplyr::select(TIME, Tair_1) %>% 
      rename(Tair = Tair_1)
    
    siteDataNew <- siteData %>% lapply(., function(x){
      if (x$metadata$instrument$id != 'THERMOCOUPLE'){
        return(x)
      } else {
        return(NULL)
      }}) %>% compact()
    
    siteDataNew[[length(siteDataNew) +1]] <-  THERMOCOUPLEsiteDataNew[[1]]
    
    siteData <- siteDataNew
  }
  
  #remove optris as this causes errors
  if ("PI160" %in% siteInf[['instId']]){
    siteInf <- siteInf %>% filter(instId != 'PI160')
  }
  
  return(list(siteInf, siteData))
}

getIntersectingSerials <- function(iIdInf, i){
  # check intersection with every serial
  intersections <- day(as.period(intersect(iIdInf[i,][['interval']], iIdInf[['interval']]), 'days'))
  #check what intersection correspong with which serial
  iIdIntersectionSerials <- iIdInf[['instSerial']][which(intersections > 0)]
  # ommit instersection with own time
  iIdIntersectionSerials <- iIdIntersectionSerials[iIdIntersectionSerials != iIdInf[i,][['instSerial']]]
  
  return(iIdIntersectionSerials)
}

getNewSiteInst <- function(iIdInf){
  #combine start and end dates for those that need combining
  combinedInsts <- iIdInf %>% filter(needsCombining == TRUE)
  
  if (nrow(combinedInsts) > 0){
    combineInstsOut <- combinedInsts %>% group_by(needsCombining) %>% 
      summarise(instSerial = paste(instSerial, collapse = '|'), sd = min(sd), 
                ed = max(ed), instId = unique(instId)) %>%
      dplyr::select(-needsCombining) %>% 
      mutate(multipleSerials = TRUE, nameChange = FALSE)
  } else {
    combineInstsOut <- combinedInsts %>% 
      dplyr::select(-c(instersectingSerials, notInstersectingSerials, needsNameChange, interval, needsCombining)) %>% 
      mutate(multipleSerials = FALSE, nameChange = FALSE)
  }
  
  #add serial to instrument id if serials overlap 
  notCombinedInsts <- iIdInf %>% filter(needsCombining == FALSE)
  notCombinedInsts <- notCombinedInsts %>% 
    dplyr::select(-c(instersectingSerials, notInstersectingSerials, needsNameChange, needsCombining, interval))
  if (nrow(notCombinedInsts) > 0){
    notCombinedInstsOut <- notCombinedInsts %>% 
      mutate(multipleSerials = FALSE, nameChange = TRUE)
  } else {
    notCombinedInstsOut <- notCombinedInsts %>%
      mutate(multipleSerials = FALSE, nameChange = FALSE)
  }
  
  # bind into one
  newSiteInst <- rbind(combineInstsOut, notCombinedInstsOut)
  
  return(newSiteInst)
}

alterInstrumentInfo <- function(iIdInf){
  #create lubridate interval
  iIdInf <- iIdInf %>% mutate(interval = interval(sd, ed))
  # init vectors
  instersectionSerials <- vector(mode = 'list', length = nrow(iIdInf))
  notInstersectionSerials <- vector(mode = 'list', length = nrow(iIdInf))
  needsCombiningVec <- c()
  needsNameChangeVec <- c()
  #for every serial
  for (i in 1:nrow(iIdInf)){
    #get all serials that instersect in time
    iIdIntersectionSerials <- getIntersectingSerials(iIdInf, i)
    #add as list entry
    instersectionSerials[[i]] <- iIdIntersectionSerials
    #add entry fpor which serials don't interect (if any)
    iIdNotIntersectionSerials <- iIdInf[['instSerial']][!(iIdInf[['instSerial']] %in% c(iIdIntersectionSerials, iIdInf[['instSerial']][i]))]
    notInstersectionSerials[[i]] <- iIdNotIntersectionSerials
    
    #if the instruments do not overlap then entries need to be combined otherwise name must be combined
    if (length(iIdIntersectionSerials) > 0 & length(iIdNotIntersectionSerials) == 0){
      needsCombining <- F
      needsNameChange <- T
      cont <- T
    } else if (length(iIdIntersectionSerials) > 0 & length(iIdNotIntersectionSerials) > 0){
      needsCombining <- T
      needsNameChange <- T
      cont <- F
    } else if (length(iIdIntersectionSerials) == 0 & length(iIdNotIntersectionSerials) > 0){
      needsCombining <- T
      needsNameChange <- F
      cont <- T
    } 
    
    needsCombiningVec <- c(needsCombiningVec, needsCombining)
    needsNameChangeVec <- c(needsNameChangeVec, needsNameChange)
  }
  
  if (any(cont == F)){
    #if there's lots at one site things get tricky .. easier to do it manually
    message(paste(unique(iIdInf[['instId']]), 'too compicated. Do manually'))
    newSiteInst <- NULL
  } else {
    # add to info 
    iIdInf[['instersectingSerials']] <- instersectionSerials
    iIdInf[['notInstersectingSerials']] <- notInstersectionSerials
    iIdInf[['needsCombining']] <- needsCombiningVec
    iIdInf[['needsNameChange']] <- needsNameChangeVec
    #get new instrument info
    newSiteInst <- getNewSiteInst(iIdInf)
  }
  
  return(newSiteInst)
}

newSerialInfo <- function(siteInf){
  
  # where there's 2 serials of the same inst - combine into 1 ( if not overlapping)
  siteInf2 <- vector(mode = 'list')
  counter <- 0
  #for every instrument
  for (iId in unique(siteInf[['instId']])){
    counter = counter + 1
    #get instrument info
    iIdInf <- siteInf %>% filter(instId == iId) 
    # check if more than 1 serial for this instrument
    if (table(siteInf[['instId']])[[iId]] > 1) {
      newSiteInst <- alterInstrumentInfo(iIdInf) 
        
      #check if couldnt work it out
      if (is.null(newSiteInst)){
        newSiteInst <- iIdInf %>% mutate(multipleSerials = TRUE, nameChange = TRUE, needsManualWork = TRUE)
      } else {
        newSiteInst <- newSiteInst %>% mutate(needsManualWork = FALSE)
      }
    } else {
      #add required columns if only 1 serial for instrument 
      newSiteInst <- iIdInf %>% mutate(multipleSerials = FALSE, nameChange = FALSE, needsManualWork = FALSE)
    }
    # add to list 
    siteInf2[[counter]] <- newSiteInst
  }
  #bind rows
  siteInf2 <- siteInf2 %>% bind_rows()
 
  return(siteInf2)
}

getCombinedData <- function(siteInf2, siteData){
  #create new list enries of combined data where there is > 2 serials of 1 instrument
  multiSerials <- siteInf2 %>% filter(multipleSerials == TRUE, needsManualWork == F)
  combinedData <- vector(mode = 'list', length = nrow(multiSerials))
  
  #check if we have anything left
  if (nrow(multiSerials) > 0){
    for (i in 1:nrow(multiSerials)){
      #get list entries with > 2 serials
      multiSerialData <- siteData %>% lapply(., function(x){
        if(x$metadata$instrument$id %in% multiSerials[i,][['instId']]){
          return(x)
        } else{
          return(NULL)
        }}) %>% compact()
      # check for any actual data
      if (length(multiSerialData) > 0) {
        #bind all data rows
        multiSerialDataD <- lapply(multiSerialData, `[[`, 1) %>% bind_rows()
        #take the first metadata entry but replace the serial no
        multiSerialDataMD <- multiSerialData[[1]][[2]]
        multiSerialDataMD$instrument$serial <- siteInf2 %>% 
          filter(multipleSerials == TRUE, instId == multiSerialDataMD$instrument$id) %>%
          dplyr::select(instSerial) %>% .$instSerial
        #append to list
        combinedData[[i]] <- list(data = multiSerialDataD, metadata = multiSerialDataMD)
      }
    }
  }
  
  return(combinedData)
}

getSiteData2 <- function(siteInf2, siteData){
  #create the combined data
  combinedData <- getCombinedData(siteInf2, siteData)
  if (length(combinedData) > 0){
    multiSerials <- siteInf2 %>% filter(multipleSerials == TRUE, needsManualWork == F)
  
    # get alldata for insts w one serial
    siteData2 <- siteData %>% lapply(., function(x){
      if(!(x$metadata$instrument$id %in% multiSerials[['instId']])){
        return(x)
      } else{
        return(NULL)}}) %>% compact()
    # combine with new data with multiple serials
    siteData2 <- append(siteData2, combinedData)
  } else {
    siteData2 <- NULL
  }
  
  return(siteData2)
}

nameChangeSiteData <- function(siteInf2, siteData2){
  nameChanges <- siteInf2 %>% filter(nameChange == TRUE, needsManualWork == F)
  # if name needs to be changed combine id and serial
  siteData2 <- siteData2 %>% lapply(., function(x){
    if(x$metadata$instrument$id %in% nameChanges[['instId']]){
      x$metadata$instrument$id <- paste(x$metadata$instrument$id, x$metadata$instrument$serial)
    }
    return(x)})
  
  return(siteData2)
}

nameChangeSiteInf <- function(siteInf2){
  
  #change name in siteInf to match siteData
  siteInf2 <- siteInf2 %>% mutate(instId = case_when(
    nameChange == TRUE ~ paste(instId, instSerial),
    TRUE ~ instId
  ))
  
  return(siteInf2)
}

checkStrangeTimeSteps <- function(instData, instByUnit, instByVal){
  #check the difference between each time step
  timeDiffs <- diff(instData$data$TIME)
  
  #change expetced time step to seconds
  if (instByUnit == 'min'){
    instByValSec <- as.numeric(instByVal) * 60
  } else {
    instByValSec = as.numeric(instByVal)
  }
  #browser()
  #find indexes where difference between time steps is not a factor of the time interval
  badTimeDiffs <- which(as.numeric(timeDiffs, units = 'secs') %% instByValSec != 0)
  #iterate until none left as sometimes this unearths more incorrect intervals
  while (length(badTimeDiffs) > 0){
    # also include before and after these bad timesteps
    badTimeDiffs2 <- c(badTimeDiffs, badTimeDiffs -1)
    badTimeDiffs3 <- c(badTimeDiffs2, badTimeDiffs +1)
    #get rid of these times
    instData$data <- instData$data[-badTimeDiffs3, ]
    print(paste(length(badTimeDiffs3), 'timesteps ommitted due to bad time differences'))
    
    timeDiffs <- diff(instData$data$TIME)
    badTimeDiffs <- which(as.numeric(timeDiffs, units = 'secs') %% instByValSec != 0)
  }
  
  return(instData)
}

qcTimeSteps <- function(instData, instByUnit, instByVal){
  # round to nearest minute
  if (instByUnit != 'sec'){
    instData$data[['TIME']] <- round_date(instData$data[['TIME']], '1 minute')
  }
  
  #get rid of rows where TIME is NA
  if (any(is.na(as.character(instData$data$TIME)))){
    instData$data <- instData$data[!is.na(as.character(instData$data$TIME)),]
  }
  # ged rid of crazy years
  if(any(as.numeric(strftime(instData$data$TIME, '%Y')) > 3000)){
    instData$data <- instData$data[as.numeric(strftime(instData$data$TIME, '%Y')) < 3000,]
  }
  #get rid of duplicated times
  if(any(duplicated(instData$data$TIME))){
    instData$data <- instData$data[!duplicated(instData$data$TIME),]
  }
  #for IMU LAS GET RID
  if (instData$metadata$instrument$id == 'LASMKII' & instData$metadata$instrument$site == 'IMU'){
    instData$data <- instData$data[as.Date(instData$data$TIME) != as.Date("2017-06-24") &
                                     as.Date(instData$data$TIME) != as.Date("2017-06-23") &
                                     as.Date(instData$data$TIME) != as.Date("2017-06-21"), ]
  }
  #check for odd time steps
  instData <- checkStrangeTimeSteps(instData, instByUnit, instByVal)
  
  return(instData)
}

getDataPresentPrec <- function(instData, siteInf2){
  message('Calculating availability')

  if (!is.null(instData)){
    #browser()
    #print(instData)
    # get the instrument info. Take first (as multiple out defs) 
    instInfo <- siteInf2 %>% 
      filter(instId == instData$metadata$instrument$id &
             instSerial == instData$metadata$instrument$serial) 
    print(paste(instInfo$instId, instInfo$instSerial))
    #start and end year
    instSy <- strftime(instInfo[['sd']], '%Y') 
    instEy <- as.character(as.numeric(strftime(instInfo[['ed']], '%Y')) + 1)
    # add space into time step e.g. 15min -> 15 min
    instByVal <- gsub("[^0-9.-]", "", instData$metadata$fileTimeRes)
    instByUnit <- gsub('[[:digit:]]+', '', instData$metadata$fileTimeRes)
    instBy <- paste(instByVal,instByUnit)
    #format into Date   
    instSd <- as.Date(paste0(instSy, '-01-01 00:00'), tz = 'UTC')
    instEd <- as.Date(paste0(instEy, '-01-01 00:00'), tz = 'UTC')
    
    # check for timesteps that wil break padding
    instData <- qcTimeSteps(instData, instByUnit, instByVal)
    #pad data 
    paddedInstData <- padr::pad(x = instData$data, interval = instBy, 
                                start_val = instSd, 
                                end_val = instEd)

    # remove last value (from the first of next year 00:00)
    paddedInstData <- paddedInstData[1:nrow(paddedInstData) - 1,]
    
    # calculate the percentage of total year data present at each time step
    presPercInstData <- paddedInstData %>% 
      dplyr::mutate(YEAR = strftime(TIME,'%Y')) %>%
      dplyr::group_by(YEAR) %>%
      mutate(yearTimeSteps = n()) %>% 
      mutate(dataPresentBool = ifelse(
        is.na(eval(parse(text=instData$metadata$units$variables))), 0, 1)) %>%
      mutate(presentAccumulation = cumsum(dataPresentBool)) %>%
      mutate(presentPercentage = (presentAccumulation/yearTimeSteps) * 100) 
    
    #select years with data in them
    dataYears <- presPercInstData %>% 
      summarize(maxPercentage = max(presentPercentage)) %>%
      dplyr::filter(maxPercentage != 0) %>%
      dplyr::select(YEAR)
      
    #check if the whole year has no data
    presPercInstData <- presPercInstData %>% 
      ungroup() %>%
      dplyr::filter(YEAR %in% dataYears[['YEAR']]) %>%
      dplyr::select(c(TIME, presentPercentage, YEAR)) %>%
      dplyr::mutate(instID = instData$metadata$instrument$id)
    
    return(presPercInstData)
  } else {
    message('No data for this entry. Skipping...')
    return(NULL)
  }
}
