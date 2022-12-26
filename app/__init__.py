from flask import Flask, render_template
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

#Declare flask app
app = Flask(__name__)
CORS(app)
#Register Blueprints
app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

#Use Config, which we created in config.py to config app
app.config.from_object(Config)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)