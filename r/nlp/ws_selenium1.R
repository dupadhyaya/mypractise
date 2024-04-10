# Web Scrapping with Selenium
#https://cbelanger.netlify.app/post/web-scraping-in-r-selenium-firefox-and-phantomjs/
pacman::p_load(RSelenium, netstat, wdman, tidyverse)

binman::list_versions(appname = 'chromedriver')
wdman:::chrome_check(verbose=T)
#binman::list_versions(appname = 'mozilla')

RSelenium::rsDriver()
#chromePath = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#rsdriverGC <- rsDriver(browser = "chrome", chromever  = "105.0.5195.19", port=free_port())
rsdriverFF <- rsDriver(browser = "firefox", port=4567L)
remdr <- remoteDriver()
remdr
remdr$port
rsdriverFF

#firefox----
rDf <- remoteDriver(browser = 'firefox')
rDf

#chrome----
rDc <- remoteDriver(browser = 'chrome')
rDc

#ie----
rDi <- remoteDriver(browser ='internet explorer')
rDi

#safari----
rDs <- remoteDriver(browser ='safari')
rDs

#start Server -----------
#RSelenium::startServer()
rDf$open()

rsCO <- rsDriverFF$client 
rsCO$navigate('http://amity.edu')

rsDriver(browser='firefox', verbose=F, chromever = NULL, port=free_port())

#brew reinstall --cask chromedriver
#'/opt/homebrew/bin/chromedriver'
#'
driver <- rD[["client"]]

# navigate to an URL
driver$navigate("http://books.toscrape.com/")

#close the driver
driver$close()

#close the server
rD[["server"]]$stop()

library(selenium)
session <- SeleniumSession$new(port = free_port())
session <- SeleniumSession$new(browser = "chrome", port = 1010L)
