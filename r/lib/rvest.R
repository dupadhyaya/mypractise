# library rvest
pacman::p_load(tidyverse, rvest)

# Start by reading a HTML page with read_html():
starwars <- read_html("https://rvest.tidyverse.org/articles/starwars.html")

# Then find elements that match a css selector or XPath expression
# using html_elements(). In this example, each <section> corresponds
# to a different film
films <- starwars %>% html_elements("section")
films
films[1]

title <- films %>% html_element("h2") %>%  html_text2()
title
films %>% html_element("p") %>%  html_text2()

episode <- films %>%  html_element("h2") %>%   html_attr("data-id") %>%  readr::parse_integer()
episode
films %>%  html_element("p") %>% html_text()


html <- read_html("https://en.wikipedia.org/w/index.php?title=The_Lego_Movie&oldid=998422565")
html
#<table class="tracklist"><tbody><tr><th class="tracklist-number-header" scope="col"><abbr title="Number">No.</abbr></th><th scope="col" style="width:60%">Title</th><th scope="col" style="width:40%">Performer(s)</th><th class="tracklist-length-header" scope="col">Length</th></tr><tr><th id="track1" scope="row">1<tr class="tracklist-total-length"><th colspan="3" scope="row"><span>Total length:</span></th><td>58:10</td></tr></tbody></table>
html %>%  html_element(".tracklist") %>%   html_table()