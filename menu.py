from bs4 import BeautifulSoup
import urllib2
import datetime

#############################
##    Menu Function     ##
#############################

def make_food_dict(url):
    """Make a dictionary with key category of food and value a list of the corresponding food items"""
    
    # Read in the url and get the html
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    
    # Get the table of the food
    tables = soup.findAll("table")
    menu = tables[2]
    
    # Get all the rows seperated
    rows = menu.findAll("tr")
    
    # Find the different category headers for food
    categories = menu.findAll("tr", { "class" : "category" })
    categories = [i.text.strip() for i in categories]
    
    # Create the dictionary
    food_dict = {}
    current_category = ""
    for row in rows:
        menu_item = row.findAll("td", { "class" : "menu_item" })
        if len(menu_item) > 0:
            food = menu_item[0].text
            food = ''.join(c for c in food if c != '|')
            food_dict[current_category].append(food.strip())
        elif row.text.strip() in categories:
            current_category = row.text.strip()
            food_dict[current_category] = []
    
    return food_dict

def food_dict_to_str(food_dict):
    """Return the food dict as a string with header of each subsection as the category and each row being a menu item"""
    return_str = ""
    for key in food_dict:
        return_str += key.upper() + "\n"
        return_str += "\n".join(food_dict[key])
        return_str += "\n\n"
    return return_str

def get_menu(day = None, meal = "lunch", categories = []):
    """Get the menu from the given inputs and turn it into a string to text back"""
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return_str = ""
    
    # Add the day of the week to the header
    if day != None and day.lower() in week_days:
        return_str += day.capitalize() + "'s "
    else:
        return_str += week_days[datetime.datetime.today().weekday()].capitalize() + "'s "
    
    return_str += meal + " "
    
    # Format the header of the menu
    if len(categories) > 2:
        return_str += ", ".join(categories[:-2])
        return_str += ", " + categories[-2] + ", and " + categories[-1]
    elif len(categories) == 2:
        return_str += categories[-2] + " and " + categories[-1]
    elif len(categories) == 1:
        return_str += categories[-1]
    return_str += "menu is\n\n"
    
    # Make the URL for the entry
    date = datetime.datetime.now()
    if day != None:
        date += datetime.timedelta(days=(week_days.index(day) - date.weekday())%7)
    url = "http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?date="
    url += str(date.month) + "-"
    url += str(date.day) + "-"
    url += str(date.year) + "&type=30&meal="
    if meal == "dinner":
        url += "2"
    elif meal == "lunch":
        url += "1"
    elif meal == "breakfast":
        url += "0"
    else:
        return "Command not found"
    
    # Make a dictionary with key the category of food and value a list of all the foods
    food_dict = make_food_dict(url)
    if len(categories) != 0:
        food_dict = {i.lower():test[i] for i in test if i.lower() in categories}
    
    # Format the body of the menu
    return_str += food_dict_to_str(food_dict)
    
    return return_str

############################
##       Top-Level        ##
############################

def makeSpecial():
    s = 'To get the menu, use the format \'menu, day (optional), meal (optional), categories of interest (optional)\'.'
    return s

## return proper format to use for getting weather
special = makeSpecial()

def eval(input):
    """Run the code"""
    
    # Parse the input
    sep = input.split(", ")
    if len(sep) == 0 or sep[0].lower() != "menu":
        return "Command not found"
    
    # No specifics asked for
    if len(sep) == 1:
        return get_menu()
    
    # If the user cared about day
    elif sep[1].lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        # If the user cared about which meal
        if len(sep) >= 3 and sep[2].lower() in ["breakfast", "lunch", "dinner"]:     
            # If the user cared about category of food
            if len(sep) > 3:
                return get_menu(day = sep[1], meal = sep[2], categories = sep[3:])
            return get_menu(day = sep[1], meal = sep[2])
        else:
            # If the user cared about category of food
            if len(sep) > 2:
                return get_menu(day = sep[1], categories = sep[2:])
            return get_menu(day = sep[1])
    else:
        # If the user cared about category
        if len(sep) > 2:
            return get_menu(meal = sep[1], categories = sep[2:])
        return get_menu(meal = sep[1])