# Web Scrapping with Selenium & Google Chrome
#https://cbelanger.netlify.app/post/web-scraping-in-r-selenium-firefox-and-phantomjs/
pacman::p_load(RSelenium, netstat, wdman, tidyverse)

binman::list_versions(appname = 'chromedriver')
rsDriver
rsdc <- rsDriver(browser = "chrome", port=free_port(), verbose = F)
#does not work
binman::app_dir('chromedriver')

binman::list_versions('chromedriver')
cpath = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
#  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
cpath2 = '/'
cver = '123.0.6312.107'
capp ='chromedriver'
binman::app_dir(appname = capp, check=T)
binman::app_dir(appname = 'firefox')
binman::list_versions()
binman::assign_directory(dllist=list(cpath), appname=capp)
rsdf$client
(driver <- rsdf[["client"]])

# navigate to an URL
driver$navigate("http://books.toscrape.com/")

#close the driver
driver$close()

#close the server
rsdf[["server"]]$stop()
