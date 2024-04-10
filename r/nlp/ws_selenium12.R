# Web Scrapping with Selenium

pacman::p_load(RSelenium, netstat, wdman, tidyverse)

binman::list_versions(appname = 'chromedriver')
driver <- rsDriver(browser = c('chrome'), chromever='123.0.6312.87', port=free_port())
RSelenium:::We
system.setProperty("webdriver.chrome.driver","/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome");
wdman:::chrome_check(verbose=T)
#binman::list_versions(appname = 'mozilla')

RSelenium::rsDriver()
#chromePath = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#rsdriverGC <- rsDriver(browser = "chrome", chromever  = "105.0.5195.19", port=free_port())
rsdriverFF <- rsDriver(browser = "firefox", port=4567L)