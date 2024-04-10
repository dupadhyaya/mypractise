# Rvest - wiki tables

pacman::p_load(rvest, tidyverse)
#https://stackoverflow.com/questions/71728023/web-scraping-with-r-rvest

urlWiki1 <- "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2002"


years <- 2003:2021
baseURL <- "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_"
urls <- paste(baseURL, years, sep = "")
urls
columns <- c("Pos.", "Equipes", "GP", "GC", "SG")
?purrr::map2_dfr
df <- purrr::map2_dfr(urls, years, ~ read_html(.x, encoding = "utf-8") %>%
    html_element('.wikitable:contains("ou rebaixamento")') %>%
    html_table() %>%   .[columns] %>%  mutate(year = .y, SG = as.character(SG)))
df


tabela <- function(link){
  read_html(link) %>% html_nodes("table.wikitable") %>% html_table()
}

urls[1]
read_html(urls[1]) %>% html_nodes('table.wikitable') %>% html_table()
read_html(urls[1]) %>% html_nodes('table') %>% .[[1]] %>% html_table()
read_html(urls[1]) %>% html_nodes('table') %>% .[[2]] %>% html_table()

all_tables = lapply(urls, tabela)
names(all_tables) <- 2003:2021
length(all_tables)
all_tables[[1]][1]

all_tables[[2]]
