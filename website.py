from app import app
import webbrowser, UeaT
from UeaT import Menu
import os

def main():
    menu_locations = os.listdir(os.path.abspath("menus"))
    if menu_locations == False:
        Menu.create_menus()
    
    Menu.load_menus(menu_locations)
    # opens the web browser
    webbrowser.open('http://localhost:5000', new=2, autoraise=True )
    # runs the app
    app.run()

if __name__ == '__main__':
    main()