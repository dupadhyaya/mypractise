# rvest - webscrapping
#https://faculty.washington.edu/otoomet/machinelearning-R/web-scraping.html
#https://github.com/yusuzech/r-web-scraping-cheat-sheet
#https://rvest.tidyverse.org/reference/index.html

pacman::p_load(rvest, httr)

basic_html <- minimal_html('
  <html>
  <head>
    <title>Page title</title>
  </head>
  <body>
    <h1 id="first">A heading</h1>
    <p class="paragraph">Some text &amp; <b>some bold text.</b></p>
    <a> Some more <i> italicized text which is not in a paragraph. </i> </a>
    <a class="paragraph">even more text &amp; <i>some italicized text.</i></p>
    <a id="link" href="www.amity.edu"> Amity University </a>
  </body>
')
basic_html

basic_html %>% html_elements(css='h1')
basic_html %>% html_elements(css='.title')
basic_html %>% html_elements(css='.paragraph')
basic_html |> html_elements(css='p.paragraph') # |> %>% same
basic_html %>% html_elements(css ='#link')
basic_html %>% html_elements(css ='a.paragraph')
basic_html %>% html_elements(css ='a.paragraph i')
basic_html %>% html_elements(css ='a.paragraph') %>% html_children()

#------
basic_html %>% html_element('p') 
basic_html %>% html_element('p') %>% writeLines()
basic_html %>% html_elements(css='p')

#--------
auLink = 'http://amity.edu'
auLink
auPage = read_html(auLink)
auPage
auSession = session(auLink)
auSession$response
content(auSession$response, as='text')
content(auSession$response, as='parsed')
content(auSession$response, as='raw')

auSession %>% html_elements('head')
auSession %>% html_elements('.country')
auSession %>% html_element('body')

auPage %>% html_elements('head')

auPage %>% html_elements('p')
auPage %>% html_elements('a') %>% html_attr('href')
auPage %>% html_elements('img') %>% html_attr('src')
auPage %>% html_elements('img') %>% html_attr('width') %>% as.integer()
auPage %>% html_elements('table') # no table

auPage %>% html_elements('b')
auPage %>% html_element('b') #first
auPage %>% html_elements('b') %>% html_text2()

df1 = data.frame(name = auPage %>% html_elements('b') %>% html_text2())
head(df1)

auPage %>% html_element('title') %>% html_text()

auPage %>% html_elements('p') %>% html_text() %>% cat()
auPage %>% html_elements("li") %>% html_attr("class", default = "inactive")
auPage %>% html_elements("li") %>% html_attr("class", default = "active")
#---------
auPage %>% html_elements('.li')
auPage %>% html_elements('[href]')
auPage %>% html_elements("section[class='home-sec2 mydiv']")
auPage %>% html_elements("div[class='student-home']") %>% html_text2()
auPage %>% html_elements("div[class='student-home']") %>% html_elements('a')
auPage %>% html_elements("div[class='student-life']") %>% html_elements('a')

auPage %>% html_element("div[class='top-home-sec1 row']") %>% html_text() %>% cat()  # add 

auPage %>% html_element('table')

#children
auPage %>% html_element('body') %>% html_children() %>% html_name()
links <- auPage %>% html_elements('a') %>% html_attr('href')
links
grep(pattern='http://www.amity.edu', links, value=T)
?grep
grep(pattern='http://amity.edu/gurgaon', links, value=T)
grep(pattern='http://', links, value=T)


auPage %>% html_elements('section')

#session------
auSession = session(auLink)
auSession

aboutAmity <- auSession %>%  session_follow_link("About Amity")
aboutAmity %>% html_elements('a') %>% html_attr('href')

aboutAmity %>% html_element("ul[class='brand-icon2']") %>% html_text2() %>% writeLines()

auSession2 <- auSession %>% session_jump_to("https://amity.edu/about-university.aspx") # go to another web page using the same session
auSession2 %>% html_elements('p a')
auSession2a <- auSession2 %>% session_follow_link(css = "p a")
auSession2a
auSession2 %>% session_follow_link(css = "p a[2]")

y_cookies_table <- cookies(my_session) # get the cookies as a table