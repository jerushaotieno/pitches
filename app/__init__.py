# from email.mime import application
from flask import Flask, app
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

    # Initializing Flask Extensions
bootstrap = Bootstrap()

db=SQLAlchemy()
photos = UploadSet('photos',IMAGES)
UPLOADED_PHOTOS_DEST ='app/static/photos'

app = Flask(__name__)

UPLOAD_FOLDER = 'app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def create_app(config_name):

    # configure UploadSet
    # configure_uploads(app,photos)
    app.config['UPLOADED_PHOTOS_DEST'] = UPLOADED_PHOTOS_DEST

    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #set up
    app.config.from_object(config_options[config_name])

    #Initialize db
    db.init_app(app)

    #reg
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app 