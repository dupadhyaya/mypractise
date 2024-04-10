# Selenium in R
#https://rpubs.com/jaketelliott/scraping-tutorial
library(RSelenium)
pacman::p_load(RSelenium, netstat, binman, tidyverse,wdman)

binman::list_versions(appname='chromedriver')

rsDvr = RSelenium::rsDriver(browser='chrome', chromever = '123.0.6312.105', port=free_port())
#rsDvr = RSelenium::rsDriver(browser='chrome', chromever = '105.0.5195.19', port=free_port())

selenium(retcommand = T)

driver <- rsDvr$client

driver$open()
driver$navigate("http://amity.edu")

page <- html_element('a')
elem <- driver$findElement(using = 'css selector', 'body > object')

drivers$close()
