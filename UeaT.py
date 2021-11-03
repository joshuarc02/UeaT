class Hall:

    def __init__(self, name, fileName):
        self.name = name
        self.names = []

        file = open(fileName)

        self.items = []
        for line in file:
            name, number = line.strip().rsplit(" ", 1)
            if name in self.names:
                continue
            self.names.append(name)
            item = Item(name, number)
            self.items.append(item)

        self.items = sorted(self.items, key=lambda item: item.name.lower())

    def update_menus():
        J2L_URL = "http://hf-food.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+Dining%3a+J2+%26+JCL&naFlag=1"
        J2L_menu = Hall.get_menu(J2L_URL)
        Hall.save_menu(J2L_menu, "J2_and_JCL_Dining")

        KIN_URL = "http://hf-food.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=03&locationName=Kins+Dining&naFlag=1"
        KIN_menu = Hall.get_menu(KIN_URL)
        Hall.save_menu(J2L_menu, "Kinsolving_Dining")
    
    def get_menu(URL):
        import requests
        from bs4 import BeautifulSoup

        page = requests.get(URL)
        page = BeautifulSoup(page.content, "html.parser")

        menu_items = page.find_all("div", class_="shortmenurecipes")
        menu_items = [item.find("span").text.strip() for item in set(menu_items)]

        return menu_items

    def save_menu(menu_items, name):
            f = open(name + "_menu.txt", "w")
            for item in menu_items:
                f.write(item + " 1\n")
            f.close()

class Item:
    def __init__(self, name, number):
        self.name = name.replace(' ', '_')
        self.number = number

    def getAvaliable(self):
        if self.number == '1':
            return '✓'
        else:
            return 'X'

    def toString(self):
        return self.name + " " + self.number

Hall.update_menus()