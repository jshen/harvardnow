import urllib2
from bs4 import BeautifulSoup
import datetime


#############################
##    Menu Function     ##
#############################

def getDateID():
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
    today215pm = now.replace(hour=14, minute=15, second=0, microsecond=0)
    today715pm = now.replace(hour=19, minute=15, second=0, microsecond=0)
    
    if now < today10am:
        menuid = 0
        date = "%s-%s-%s" % (now.month, now.day, now.year)
    elif now > today10am and now < today215pm:
        menuid = 1
        date = "%s-%s-%s" % (now.month, now.day, now.year)
    elif now > today215pm and now < today715pm:
        menuid = 2
        date = "%s-%s-%s" % (now.month, now.day, now.year)
    else :
        menuid = 0
        date = "%s-%s-%s" % (tomorrow.month, tomorrow.day, tomorrow.year)
    return menuid, date


def getAllMenu(menuid, date):
    food_nvg = []
    food_veg = []
    food_vgn = []
    unwanted = ['ACCOMPANIMENTS & FRUIT','SPECIAL BARS - BOARD MENU','Cereals',
                'Breads','Cheese','Yogurts, Jams and Spreads','Dressings',
                'Beverages','BREAKFAST BREADS','SALAD BAR','SANDWICH BAR',
                'DESSERTS','FROM THE GRILLE','ENTREE SALADS','SIDE SALADS',
                'CULINARY DISPLAY']
    url = 'http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?'
    url += 'date=%s&type=30' %date
    url += '&meal=%i' %menuid
    website = urllib2.urlopen(url)
    soup = BeautifulSoup(website.read(), 'html.parser') 
    letters = soup.find_all("table")
    menutable = letters[2]
    category_real = menutable.find("tr", class_="category")
    category = str(category_real.get_text().strip('\t\r\n\''))
    menu = category_real.next_sibling.next_sibling
    cont = True
    while cont == True:
        if category in unwanted:
            while cont == True and 'class' not in menu.attrs:
                menu = menu.next_sibling.next_sibling
                if not menu:
                    cont = False
                else:
                    cont = True
            if cont == True:
                category = str(menu.get_text().strip('\t\r\n\'')) 
                menu = menu.next_sibling.next_sibling
        else:
            while cont == True and 'class' not in menu.attrs:
                menuitem = str(menu.a.get_text().strip('\t\r\n\''))
                vegn_check = menu.find_all("img")
                if not vegn_check:
                    food_nvg.append(menuitem)
                else:
                    if menuitem == 'Mayonnaise':
                        food_veg.append(menuitem)
                        food_vgn.append(menuitem)
                    elif len(vegn_check) == 1:
                        food_veg.append(menuitem)
                    else:
                        food_veg.append(menuitem)
                        food_vgn.append(menuitem)
                menu = menu.next_sibling.next_sibling
                if not menu:
                    cont = False
                else:
                    cont = True
            if cont == True:
                category = str(menu.get_text().strip('\t\r\n\'')) 
                menu = menu.next_sibling.next_sibling
            
    return food_veg, food_nvg, food_vgn

def getMenu(input):
    menuid,date = getDateID()
    food_veg, food_nvg, food_vgn = getAllMenu(menuid,date)
    
    if menuid == 0:
        meal = 'Breakfast'
    elif menuid == 1:
        meal = 'Lunch'
    elif menuid == 2:
        meal = 'Dinner'
    
    if input == 'veg':
        body = meal + ': Vegetarian'
        for item in food_veg:
            body += '\n   ' + item 
        return body
    elif input == 'nvg':
        body = meal + ': NonVeg'
        for item in food_nvg:
            body += '\n   ' + item 
        return body
    elif input == 'vgn':
        body = meal + ': Vegan'
        for item in food_vgn:
            body += '\n   ' + item 
        return body


############################
##       Top-Level        ##
############################
     
def makeSpecial():
    s = "You can type any of the keyword below to get menus:\n"\
    "\'food veg\' for vegetarian options\n"\
    "\'food vgn\' for vegan options \n"\
    "\'food nvg\' for non-vegetarian options\n"
    return s

## return proper format to use for getting weather
special = makeSpecial()
    
def eval(input):
    return getMenu(input)



        
    
    

    




