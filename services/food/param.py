# dictionary of URL parameters associated with each keyword
# parameter = param[keyword.upper()]
param = {
  "BREAKFAST" : "type=30&meal=0&"
  "LUNCH"     : "type=30&meal=1&"
  "CHILI"     : "type=08&meal=0&"
  "DINNER"    : "type=30&meal=2&"
  "PASTA"     : "type=08&meal=1&"
  "FLYBY"     : "type=29&meal=0&"
  "BAGMEAL"   : "type=09&meal=0&"
  
}

# dictionary of menu categories to scrape
# categories = scrape[keyword.upper()]
# WARNING - SUNDAY HAS CONTINENTAL BREAKFAST
scrape = {
  "BREAKFAST" : {
    "BREAKFAST MEATS",
    "BREAKFAST ENTREES",
    "BREAKFAST BAKERY",
    "STARCH & POTATOES",
    "ACCOMPANIMENTS & FRUIT",
    "MAKE OR BUILD YOUR OWN"
  }
  
  "LUNCH"     : {
    "TODAY'S SOUP",
    "ENTREES",
    "VEGETARIAN ENTREE",
    "STARCH & POTATOES",
    "VEGETABLES",
    "DESSERTS",
    "BEAN, WHOLE GRAIN",
    "ENTREE SALADS",
    "SIDE SALADS"
  }
  
  "CHILI"     : "CHILI BAR"
  
  "DINNER"    : {
    "TODAY'S SOUP",
    "ENTREES",
    "VEGETARIAN ENTREE",
    "STARCH & POTATOES",
    "VEGETABLES",
    "DESSERTS",
    "BEAN, WHOLE GRAIN",
    "CULINARY DISPLAY",
    "ENTREE SALADS",
    "SIDE SALADS"
  }
  
  "PASTA"     : "WHOLE GRAIN PASTA BAR"  
  "FLYBY"     : "TODAY'S SOUP"
}

# list of menu items to omit
# because they are available every single day
# or are too vague to be useful
omit = {
  "Cage Free Eggs Cooked to Order",
  "Cage-Free Egg Whites Cooked to Order",
  "Plain Omelette",
  "Scrambled Cage Free Eggs",
  "Hard Cooked Eggs - Cage Free",
  "Chefs Choice"
}
