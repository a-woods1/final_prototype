from flask import render_template
from flask_login import login_required

#This is our blueprint we setup in __init__.py
from . import home

@home.route('/')
#@login_required
def homepage():
    """
        Render the homepage template on the / route
        """
    return render_template('base.html', script_name='home.js', title="Welcome")
