from flask import Flask

#Initializing application
app= Flask(__name__)

#Avoiding circular imports

from app import views