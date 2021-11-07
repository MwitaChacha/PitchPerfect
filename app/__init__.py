from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


app = Flask(__name__,instance_relative_config = True)

bootstrap = Bootstrap(app)
from app import views