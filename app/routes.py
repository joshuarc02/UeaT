# sets up how the website flows
from flask import render_template, flash, redirect, request, url_for, session, send_file
from app import app
import os, sys
from UeaT import *


# home page stuff
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    # initalizing all the vars for the page
    session['J2_and_JCL_Dining'] = Hall('J2_and_JCL_Dining', 'J2_and_JCL_Dining_menu.txt')
    session['Kinsolving_Dining'] = Hall('Kinsolving_Dining', 'Kinsolving_Dining_menu.txt')

    # renders the given template and then defines vars
    return render_template('index.html', title='Home')


@app.route('/generic', methods = ['GET', 'POST'])
def generic():
    name = request.args.get('hall')
    menu = session[name].items
    if request.method == 'POST':
        f = open("demofile2.txt", "a")
        for item in menu:
            avaliable = request.form[item.name]
            if avaliable:
                item.number = '1'
            else:
                item.number = '0'
            
            f.write(item.toString())
        f.close()
        return redirect(url_for('generic'))


    name = name.replace('_', ' ')
    # renders the given template and then defines vars
    return render_template('generic.html', title='Home', name=name, menu=menu)

@app.route('/elements', methods = ['GET', 'POST'])
def elements():
    # renders the given template and then defines vars
    return render_template('elements.html', title='Home')