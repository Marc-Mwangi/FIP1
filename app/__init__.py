from flask import Flask
#importing configurations
from .config import Development
from flask_bootstrap import Bootstrap

#Initializing application
app= Flask(__name__)

#Setting up configuration
app.config.from_object(Development)

bootstrap = Bootstrap(app)
#Avoiding circular imports

from app import views