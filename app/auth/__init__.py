from flask import Blueprint

auth = Blueprint('auth', __name__)

#This is the views.py from the auth directory.
from . import views
