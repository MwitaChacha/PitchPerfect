import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:6775@localhost/trial'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:6775@localhost/trial'
    SECRET_KEY = 'thisismysecret'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 