# extract from web pages
#https://rvest.tidyverse.org/articles/harvesting-the-web.html
#https://rvest.tidyverse.org/articles/harvesting-the-web.html#extracting-html-elements-with-xpath-1
#https://r4ds.hadley.nz/webscraping

pacman::p_load(xml2, rvest, purrr, stringr)

link1 = '/Users/du/dup/analytics/projects/mypractise/data/xmlFile.html'
htmlDump = read_html(link1)
htmlDump

class(htmlDump)
htmlDump %>% html_nodes(xpath='/bookstore') %>% html_text2()

xhtmlDump = minimal_html(link1)
xhtmlDump

xhtmlDump %>% html_text()
xhtmlDump %>% html_node('table') %>% html_text2()
