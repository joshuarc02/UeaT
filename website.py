from app import app
import webbrowser, UeaT
from UeaT import Menu
import os


def main():
    # opens the web browser
    webbrowser.open('http://localhost:5000', new=2, autoraise=True )
    # runs the app
    app.run()


if __name__ == '__main__':
    main()