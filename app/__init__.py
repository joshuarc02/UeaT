# basically just iniatializes the website i think

from flask import Flask
from config import Config
from flask_session import Session

sess = Session()
# starts the app
app = Flask(__name__, template_folder='templates')
# sets the config
app.config.from_object(Config)
# sets up the session
sess.init_app(app)
# gets the website routes and db layout
from app import routes
