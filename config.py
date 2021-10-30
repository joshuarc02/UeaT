# sets up config vars
from os import environ, path
# gets where this file is?
basedir = path.abspath(path.dirname(__file__))

class Config(object):
    # setting up the secret key for something i think cryptography
    SECRET_KEY = 'you-will-never-guess' #or environ.get('SECRET_KEY')
    # makes session happy :)
    SESSION_TYPE = 'filesystem'  #environ.get('SESSION_TYPE')