import os

class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/pitches'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST ='app/static/photos'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

