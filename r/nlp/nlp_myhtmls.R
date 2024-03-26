# NLP - mydata
pacman::p_load(tidyverse, rvest)

# Start by reading a HTML page with read_html():
urllocal = 'Users/du/dup/analytics/projects/mypractise/data/student2.html'
urlLink =  'https://raw.githubusercontent.com/dupadhyaya/mypractise/main/data/student2.html'

sthtml <- read_html(urlLink)
sthtml

# Then find elements that match a css selector or XPath expression
# using html_elements(). In this example, each <section> corresponds
# to a different film
sthtml %>% html_elements('h1') %>% html_text2()
sthtml %>% html_elements('table') %>% html_text2()

#select table using css selector
sthtml %>% html_nodes('table') %>% .[[1]] 
sthtml %>% html_nodes('table') %>% .[[1]] %>% html_table()


title <- films %>% html_element("h2") %>%  html_text2()
title