# Xpath method 
#https://www.opencodez.com/how-to-guide/how-to-use-xpath-for-web-scraping-with-r.htm
library(XML)
#https://search.r-project.org/CRAN/refmans/xml2/html/xml_find_all.html
url <- "https://www.opencodez.com/"
source <- readLines(url, encoding = "UTF-8")
source[1:4]
parsed_doc <- htmlParse(source, encoding = "UTF-8")

xpathSApply(parsed_doc, path = '/html/body/div[2]/div/div/div/div[1]/div[1]/article[1]/header/h2/a', xmlValue)

#correct path - absolute
xpathSApply(parsed_doc, path = '/html/body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/article[1]/header/h2/a', xmlValue)

#other way wild card----
(xpathSApply(doc = parsed_doc, path ="//h2/*", xmlValue))[1]

#Position----
xpathSApply(doc = parsed_doc, path ="//h2[position()=1]", xmlValue)[1]

#Last---
xpathSApply(doc = parsed_doc, path ="//h2[last()]", xmlValue)[1]

#Count----
xpathSApply(parsed_doc,"//h2[count(.//a)>0]", xmlValue)[1]

#TextBased ----
library(stringr)
#contains
xpathSApply(parsed_doc,"//a[contains(text(), '10')]", xmlValue)
xpathSApply(parsed_doc,"//a[contains(text(), 'Python')]", xmlValue)
#starts-wth
xpathSApply(parsed_doc,"//a[starts-with(./@title, '10')]", xmlValue)
xpathSApply(parsed_doc,"//a[starts-with(./@title, 'Python')]", xmlValue)


#XnodeRelations----
xpathSApply(parsed_doc,"//a/ancestor::article", xmlValue)
xpathSApply(parsed_doc,"//div[position()=1]/child::article", xmlValue)


#xmlfind------
library(xml2)
x <- read_xml("<foo><bar><baz/></bar><baz/></foo>")
x
xml_find_all(x, ".//baz")
xml_path(xml_find_all(x, ".//baz"))

# Note the difference between .// and //
# //  finds anywhere in the document (ignoring the current node)
# .// finds anywhere beneath the current node
(bar <- xml_find_all(x, ".//bar"))
xml_find_all(bar, ".//baz")
xml_find_all(bar, "//baz")

x2 <- read_html(url)
x2
xml_find_all(x2, ".//h2", flatten=T)
xml_path(xml_find_all(x2, './/h2'))

#https://campus.datacamp.com/courses/web-scraping-in-r/advanced-selection-with-xpath?ex=9


#selectr-----
library(selectr)
