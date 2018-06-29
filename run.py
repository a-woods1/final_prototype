import os #We need this to get the OS ENV VARIABLE 'FLASK_CONFIG'
 
#You are going to import the create_app from the __init__.py file
from app import create_app
 
#In our environment variables we create "FLASK_CONFIG" and set our value either development or production
config_name = os.getenv('FLASK_CONFIG')
#app = create_app('development')
 
if __name__ == '__main__':
    app.run()
