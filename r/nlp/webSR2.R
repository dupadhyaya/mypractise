# extract from web pages
#https://rvest.tidyverse.org/articles/harvesting-the-web.html
#https://rvest.tidyverse.org/articles/harvesting-the-web.html#extracting-html-elements-with-xpath-1
pacman::p_load(xml2, rvest, purrr, stringr)

link1 = 'http://www.imdb.com/title/tt1490017/'

htmlDump = read_html(link1)
#htmlDump

htmlDump %>% html_nodes("*") %>% html_attr("class") %>% unique()
htmlDump %>% html_nodes("*") %>% html_attr("id") %>% unique()
htmlDump %>% html_nodes('.cast_list') %>% html_name()
characters <- html_nodes(htmlDump, ".cast_list .character")
length(characters)
htmlDump %>% html_nodes('.ipc-voting__label__text') %>% html_text()
htmlDump %>% html_nodes('.ipc-list-card__actions') %>% html_text()
htmlDump %>% html_nodes('.ipc-title__text') %>% html_text()
htmlDump %>% html_nodes('.ipc-title__text +') %>% html_text()
