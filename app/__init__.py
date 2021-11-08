from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand
# from flask-script import Manager


app = Flask(__name__,instance_relative_config = True)
app.config['SECRET_KEY'] = 'thisismysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:6775@localhost/trial'
app.config['DATABASE_URL'] = 'postgresql+psycopg2://postgres:6775@localhost/trial'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
from app import views