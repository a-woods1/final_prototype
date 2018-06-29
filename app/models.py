from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
 
from app import db
 
class User(UserMixin, db.Model):
    """
    Create a Users table
    """
 
    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
 
    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')
 
    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)
 
    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)
 
    def __repr__(self):
        return ''.format(self.username)
