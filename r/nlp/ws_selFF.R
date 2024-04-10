# Web Scrapping with Selenium & Mozilla Firefox
#https://cbelanger.netlify.app/post/web-scraping-in-r-selenium-firefox-and-phantomjs/
pacman::p_load(RSelenium, netstat, wdman, tidyverse)

#binman::list_versions(appname = 'mozilla')

rsdf <- rsDriver(browser = "firefox", port=free_port(), verbose=F)
rsdf$client
(driver <- rsdf[["client"]])

# navigate to an URL
#driver$navigate("http://books.toscrape.com/")

#close the driver
#driver$close()

#close the server
#rsdf[["server"]]$stop()
driver$navigate("https://amity.edu")
pacman::p_load(rvest, tidyverse)
html <- driver$getPageSource()[[1]]
read_html(html) %>% html_nodes('a')

driver$navigate("http://www.bbc.co.uk")
driver$findElements(value ='//frame')
webElement <- driver$findElements(using='name', value='contents')
webElement$elementId
