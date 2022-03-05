from flask import Flask
from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

# #App initialization
# app = Flask(__name__)

# # Configuration setup
# app.config.from_object(DevConfig)

# from app import views 
# from app import errors

# # Initializing application
# app = Flask(__name__,instance_relative_config = True)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile("config.py")

# # Initializing Flask Extensions
# bootstrap = Bootstrap(app)

def create_app(config_name):
    app = Flask(__name__)

    #set up
    app.config.from_object(config_options[config_name])

    #reg
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app 