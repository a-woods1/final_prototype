from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_webpack import Webpack
import os
 
#Importing from the config.py
from config import app_config
 
# db variable initialization
db = SQLAlchemy()
 
#The flask login manager
login_manager = LoginManager()
 
webpack = Webpack()
 
def create_app(config_name):
    #This will be either "development" or "production" mapped to what we write in the config.py application
    #static_folder is where the static folder will be located
    config_name = "development"
    app = Flask(__name__, instance_relative_config=True, static_folder=os.path.join(os.getcwd(), "static"))
    print('Running in %s' % (config_name))
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    #You need a secret key to be able to utilise the database connection
    app.secret_key = 'Awesome App'
    Bootstrap(app)
    db.init_app(app)
    #This will make it so our chunked js files are able to be loaded on the template
    app.config.update({'WEBPACK_MANIFEST_PATH': '../manifest.json'})
    webpack.init_app(app)
 
    #if a user tries to access a page that they are not authorized to, it will redirect to the specified view and display the specified message.
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    #auth.login is not the route but actually the class path.
    login_manager.login_view = "auth.login"
    
    #This let's us do our migrations
    migrate = Migrate(app, db)
 
    #Bring in our new tables
    from app import models
 
    #Our blueprints for our app
 
    #This is how you get authenticated
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
	
    #Bring in the home module
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
 
    return app
