from flask import Flask
from config import DevConfig

#App initialization
app = Flask(__name__)

# Configuration setup
app.config.from_object(DevConfig)

from app import views 
from app import errors