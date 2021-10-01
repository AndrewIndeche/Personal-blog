import os
from dotenv import load_dotenv
load_dotenv()

        #email config
class Config:
    '''
    '''
    SECRET_KEY = os.urandom(32)
    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DEBUG = True

class ProductionConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://andrew:Vixen123@localhost/blog'

class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
