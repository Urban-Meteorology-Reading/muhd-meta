library(analysisToolsLUMA)
library(plyr)
library(dplyr)
library(processx)
library(RSQLite)
library(lubridate)
library(ggplot2)
library(purrr)
library(pals)
library(htmlwidgets)
library(plotly)
library(httr)
library(jsonlite)

source('scripts/makeAvailabilityPlotFunctions.R')

#### a space separated file of username and password for LUMA web products
credentialsFile <- 'scripts/credentials.txt'
#get sites from api 
LUMAsiteIDs <- getLUMAsiteIDs(credentialsFile)

#specify which sites the plots have already been created (to save going through all)
done <- c()

for (siteId in LUMAsiteIDs){
  print(siteId)
  if (siteId %in% done){
    print('done')
    next
  }
  #get start and end date for every instrument at every site
  siteInf <- getSiteInf(siteId) 
  
  if(is.null(siteInf)){
    next
  } else {
    siteInf <- siteInf %>% filter(instId != 'TINYTAG' & instId != 'KH20')
  }
  #info to submit to analysis tools luma
  instVars <- getInstVar()
  
  #get data for each instrument
  siteData <- vector(mode = 'list', length = nrow(siteInf))
  # for every instrument
  for (i in 1:nrow(siteInf)){
    inst <- siteInf[i,]
    if (inst[['instId']] %in% instVars[['instId']]){
      # get the data
      instData <- getInstData(inst, instVars)
      #append to list 
      siteData[[i]] <- instData
    } else {
      message(paste('Not able to process', inst[['instId']], '. Skipping...'))
    }
  }
  
  # get rid of null entries (instrument not present in instVars)
  siteData <- siteData %>% compact()
  
  #do manual changes (cheeky tricks)
  manualInfo <- manualInfoChange(siteId, siteData, siteInf)
  siteInf <- manualInfo[[1]]
  siteData <- manualInfo[[2]]
  
  # create an altered site info for sites where theres 2 serials for same instrument
  siteInf2 <- newSerialInfo(siteInf)
  #siteInf2 <- siteInf2 %>% mutate(needsManualWork = F, multipleSerials = F)
  #combine data and metadata for instruments w multiple serials and add this to siteData
  if (any(siteInf2[['multipleSerials']])){
    siteData2 <- getSiteData2(siteInf2, siteData)
  } else {
    siteData2 <- siteData
  }
  
  if(is.null(siteData2) | length(siteData2) == 0){
    print('siteData2 empty')
    done <- c(done, siteId)
    next
  }
  #if two serials of same instrument deployed at same time change the name
  if (any(siteInf2[['nameChange']])){
    siteData2 <- nameChangeSiteData(siteInf2, siteData2)
    siteInf2 <- nameChangeSiteInf(siteInf2)
  }
  
  #get daily availability
  dataAvailability <- siteData2 %>%
     lapply(getDataPresentPrec, siteInf2) %>% 
     bind_rows() 
  
  #calculate daily mean
  dailyDataAvailability <- dataAvailability %>% 
    mutate(DOYYEAR = strftime(TIME, '%j-%Y')) %>%
    group_by(instID, DOYYEAR) %>% 
    dplyr::summarise(dailyPresentPercentage = mean(presentPercentage), YEAR = unique(YEAR)) %>%
    mutate(TIME = as.POSIXct(DOYYEAR, format='%j-%Y')) %>%  
    mutate(dailyPresentPercentage = plyr::round_any(dailyPresentPercentage, 0.1))
  
  # font
  f <- list(family = "Arial, Narrow Regular",
            size = 15)
  
  #axis layouts
  xaxisLayout <- list(title = "Date")
  yaxisLayout <- list(title = "Percentage of maximum possible <br> data present in year (%)")
  #for adding title - as a hacky annotation
  legendTitle <- list(yref='paper',xref="paper",y=0.85,x=1.15, text="Instrument ID",showarrow=F)
  #for adding last run time - as a hacky annotation
  dtNow <- paste("Last updated: <br>", as.character(Sys.Date()))
  lastUpdate <- list(yref='paper',xref="paper",y=-0.1,x=1.15, text=dtNow,showarrow=F)
  
  #create color ramp from "random colors"
  color = grDevices::colors()[grep('gr(a|e)y|white', grDevices::colors(), invert = T)]
  set.seed(8)
  samp <- sample(1:length(color), 30)
  cr <- color[samp]
  cr[1] <- "royalblue"
  #pie(rep(1,length(cr)), col =cr)
  cr <- setNames(cr, unique(dailyDataAvailability$instID))
  #set margin
  m <- list(
    r = 200
  )
  #create plotly plot
  dailyDataAvailabilityPlot <- plot_ly(dailyDataAvailability, x=~TIME,y=~dailyPresentPercentage,
                                       color = ~instID, name = ~instID,
                                       text = ~paste("Date:", TIME, "<br>Data available:", dailyPresentPercentage,
                                                     "% <br>Instrument ID:", instID),
                                       colors = cr, width = 1120, height = 520) %>%
                              add_markers() %>%
                              layout(showlegend = T, font = f,
                                     legend=list(y=0.8, yanchor="top" ),
                                     xaxis = xaxisLayout, yaxis = yaxisLayout,
                                     annotations=list(legendTitle, lastUpdate),
                                     margin = m)
  # save html file
  htmlwidgets::saveWidget(as_widget(dailyDataAvailabilityPlot), 
                          file.path('source', '_static', 'availability_plots',
                                    paste0(siteId, '_availability.html')), 
                          selfcontained = F, libdir = "libs")
  
  done <- c(done, siteId)
  "Sleeping..." 
  Sys.sleep(120)
}

