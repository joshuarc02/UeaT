# sets up how the website flows
from flask import render_template, flash, redirect, request, url_for, session, send_file
from app import app
import os, sys
from UeaT import *

# globals
@app.context_processor
def add_info():
    if not Menu.menus:
        Menu.load_menus()

    return {
        "menus": [menu.name for menu in Menu.menus]
    }

# home page stuff
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    # renders the given template and then defines vars
    return render_template(
        'index.html',
        title='Home',
    )


@app.route('/generic', methods = ['GET', 'POST'])
def generic():
    name = request.args.get('menu').replace('_', ' ')
    if name == 'None':
        name = session['current_menu']
    session['current_menu'] = name

    menu_location = Menu.get_menu_location(name)

    menu = Menu(name, menu_location)
    
    if request.method == 'POST':
        f = open(menu_location, "w")
        
        for item in menu.items:
            avaliablitity = request.form.get(item.name)
            item.update_avaliablitity(avaliablitity)
            f.write(item.toString() + "\n")
        f.close()


    # renders the given template and then defines vars
    return render_template(
        'generic.html', 
        title='Home', 
        name=name.replace('_', ' '),
        menu=menu.items
    )