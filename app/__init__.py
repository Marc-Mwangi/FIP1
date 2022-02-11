from flask import Flask
#importing configurations
from .config import Development
from .models import *

#Initializing application
app= Flask(__name__)

#Setting up configuration
app.config.from_object(Development)

#Avoiding circular imports

from app import views