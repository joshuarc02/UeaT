# sets up how the website flows
from flask import render_template, flash, redirect, request, url_for, session, send_file
from app import app
import os, sys
from UeaT import *


# home page stuff
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    # renders the given template and then defines vars
    return render_template('index.html', title='Home')


@app.route('/generic', methods = ['GET', 'POST'])
def generic():
    name = request.args.get('hall')
    if name == 'None':
        name = session['current_hall']
    session['current_hall'] = name

    print(name)

    hall = Hall(name, name + '_menu.txt')
    
    if request.method == 'POST':
        f = open(name + "_menu.txt", "w")
        avaliable = request.form.getlist("items")
        print(avaliable)
        for item in hall.items:
            if item.name in avaliable:
                item.number = '1'
            else:
                item.number = '0'
            
            f.write(item.toString() + "\n")
        f.close()
        return render_template('index.html', title='Home')


    # renders the given template and then defines vars
    return render_template('generic.html', title='Home', name=name.replace('_', ' '), menu=hall.items)