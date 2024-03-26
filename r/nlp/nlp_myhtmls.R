# NLP - mydata
pacman::p_load(tidyverse, rvest)

# Start by reading a HTML page with read_html():
urllocal = 'Users/du/dup/analytics/projects/mypractise/data/student2.html'
urlLink2 =  'https://raw.githubusercontent.com/dupadhyaya/mypractise/main/data/student2.html'
urlLink3 =  'https://raw.githubusercontent.com/dupadhyaya/mypractise/main/data/student3.html'
#show as webpage
#https://html-preview.github.io/?url=https://github.com/dupadhyaya/mypractise/blob/main/data/student3.html

sthtml2 <- read_html(urlLink2)
sthtml2

# Then find elements that match a css selector or XPath expression
# using html_elements().
sthtml2 %>% html_elements('h1') %>% html_text2()
sthtml2 %>% html_elements('table') %>% html_text2()

#select table using css selector
sthtml2 %>% html_nodes('table') %>% .[[1]] 
sthtml2 %>% html_nodes('table') %>% .[[1]] %>% html_table()

#student3-----
sthtml3 <- read_html(urlLink3)
sthtml3
sthtml3 %>% html_elements('h1') %>% html_text2()
sthtml3 %>% html_elements('table') %>% html_text2()
sthtml3 %>%  html_element("p") %>% html_text()

#select table using css selector
sthtml3 %>% html_nodes('table') %>% .[[1]] 
sthtml3 %>% html_nodes('table') %>% .[[1]] %>% html_table()
sthtml3 %>% html_nodes('table') %>% .[[1]] 
sthtml3 %>% html_nodes(xpath="//table[@class='tbl']") %>% html_table()
#sthtml3 %>% html_nodes(xpath="//*[@class='tbl']/table[1]") %>% html_table()
#//p | //th+//th
sthtml3 %>% html_nodes(xpath="//table") %>% html_table()

#usingSelenium-----
#library(selenium)
pacman::p_load(RSelenium, purrr, rvest, glue)
#https://www.java.com/en/download/
system('java -version')
