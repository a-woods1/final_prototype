from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from .. import db, login_manager
from ..models import User
from . import auth

class RegistrationForm(FlaskForm):
  """
  Form for users to create new account
  """
  email = StringField('Email', validators=[DataRequired(), Email()])
  username = StringField('Username', validators=[DataRequired()])
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
  confirm_password = PasswordField('Confirm Password')
  submit = SubmitField('Register')
                                                     
def validate_email(self, field):
  if User.query.filter_by(email=field.data).first():
    raise ValidationError('Email is already in use.')

def validate_username(self, field):
  if User.query.filter_by(username=field.data).first():
    raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
  """
  Form for users to login
  """
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')

@login_manager.user_loader
def load_user(id):
  #This is the how we locate the user in our testApp database
  return User.query.get(int(id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email=form.email.data, username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=form.password.data)
    # add user to the database
    db.session.add(user)
    db.session.commit()
    flash('You have successfully registered! You may now login.')
    # redirect to the login page
    return redirect(url_for('auth.login'))
    
  # load registration template
  return render_template('register.html', form=form, title='Register')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    # check whether user exists in the database and whether
    # the password entered matches the password in the database
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      # log user in
      login_user(user)
      # redirect to the dashboard page after login
      return redirect("/")
      # when login details are incorrect
    else:
      flash('Invalid email or password.')
  # load login template
  return render_template('login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
  """
  Handle requests to the /logout route
  Log an user out through the logout link
  """
  logout_user()
  flash('You have successfully been logged out.')
    
  # redirect to the login page
  return redirect(url_for('auth.login'))
