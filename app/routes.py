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
    session['J2_JCL'] = Hall('J2_JCL', 'J2_JCL_menu.txt')
    session['Kins'] = Hall('Kins', 'Kins_menu.txt')

    # renders the given template and then defines vars
    return render_template('index.html', title='Home')


@app.route('/generic', methods = ['GET', 'POST'])
def generic():
    # renders the given template and then defines vars
    return render_template('generic.html', title='Home')

@app.route('/elements', methods = ['GET', 'POST'])
def elements():
    # renders the given template and then defines vars
    return render_template('elements.html', title='Home')