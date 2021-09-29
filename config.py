import os
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
        #email config
class Config:
    '''
    '''
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
