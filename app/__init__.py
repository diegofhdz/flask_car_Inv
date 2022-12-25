from flask import Flask
from .site.routes import site
from config import Config

#Declare flask app
app = Flask(__name__)
#Use Config, which we created in config.py to config app
app.config.from_object(Config)

#Register Blueprints
app.register_blueprint(site)