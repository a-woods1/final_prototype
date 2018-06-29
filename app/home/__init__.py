from flask import Blueprint

home = Blueprint('home', __name__)

#This is the views.py from the home directory.
from . import views
