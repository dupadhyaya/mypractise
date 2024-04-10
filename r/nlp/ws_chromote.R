
library(chromote)

b <- ChromoteSession$new()

# In a web browser, open a viewer for the headless browser. Works best with
# Chromium-based browsers.
b$view()

b$Page$navigate("https://www.r-project.org/")

# Saves to screenshot.png
b$screenshot()
