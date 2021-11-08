from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,instance_relative_config = True)
app.config['SECRET_KEY'] = 'thisismysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:6775@localhost/trial'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


from app import views