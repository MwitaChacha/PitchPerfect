from flask import Flask
from .config import DevConfig



app = Flask(__name__,instance_relative_config = True)


from app import views