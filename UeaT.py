class Menu:
    menus_folder = "/menus/"
    menus = []

    def __init__(self, name, file_location=None):
        self.name = name
        self.items = []

        if file_location:
            file = open(file_location)

            for line in file:
                name, number = line.strip().rsplit(" ", 1)

                item = Item(name, number)
                self.items.append(item)

    def load_menus():
        import os

        menu_locations = os.listdir(os.path.abspath("menus"))
        if not menu_locations:
            Menu.create_menus()
            menu_locations = os.listdir(os.path.abspath("menus"))

        for location in menu_locations:
            name = location.replace('.txt', '')
            menu_location = Menu.get_menu_location(name)
            menu = Menu(name, menu_location)
            Menu.menus.append(menu)
        
    def create_menus():
        import requests
        from bs4 import BeautifulSoup
        food_URL = "http://hf-food.austin.utexas.edu/foodpro/"
        locations_URL = food_URL + "location.aspx"
        
        # getting the page
        page = requests.get(locations_URL)
        page = BeautifulSoup(page.content, "html.parser")

        # getting the locations
        locations = page.find_all("span", class_="locationchoices")
        locations = [location.find("a") for location in locations]
        
        # creating each of the menus
        for location in locations:
            # getting the menu
            location_URL = food_URL + location['href']
            menu = Menu.get_menu(location_URL)

            # creating and saving the menu
            Menu.create_menu(menu, location.text)
    
    def get_menu(URL):
        import requests
        from bs4 import BeautifulSoup

        # getting the page
        page = requests.get(URL)
        page = BeautifulSoup(page.content, "html.parser")

        # getting the menu items text
        menu_items = page.find_all("div", class_="shortmenurecipes")
        menu_items = [item.find("span").text.strip() for item in set(menu_items)]
        menu_items = sorted(menu_items)

        return menu_items

    def create_menu(menu_items, name):
        name = name.replace('&', 'and').replace(':', '')

        file_location = Menu.get_menu_location(name)

        # going throught the items
        menu = Menu(name)
        f = open(file_location, "w")
        for item_text in menu_items:
            item = Item(item_text)
            menu.items.append(item)
            f.write(item.toString() + "\n")
        f.close()

        return menu 

    def get_menu_location(name):
        import os
        return os.path.abspath("menus/" + name + '.txt')
            

class Item:
    def __init__(self, name, number = 1):
        self.name = name
        self.number = int(number)

    def getAvaliable(self):
        if self.number > 0:
            return '✓'
        else:
            return 'X'

    def toString(self):
        return self.name + " " + str(self.number)