# sets up how the website flows
from flask import render_template, flash, redirect, request, url_for, session, send_file
from app import app
import os, sys
from UeaT import *


# home page stuff
@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    if  request.method == 'POST':
        # getting selected topics and redirecting to the setup page
        topics = request.form.getlist('topics')
        if topics == []:
            return redirect(url_for('index'))
        session['topics'] = [topic.replace("_", " ") for topic in topics]
        return redirect(url_for('question_setup'))

    # initalizing all the vars for the page
    J2_JCL = Hall('J2_JCL', 'J2_JCL_menu.txt')
    Kins = Hall('Kins', 'Kins_menu.txt')

    # renders the given template and then defines vars
    return render_template('index.html', title='Home', items=J2_JCL.items)
