from flask import render_template,request,redirect,url_for
from app import app
from flask_wtf import FlaskForm
from .forms import LoginForm, RegisterForm, PitchForm, CommentForm
from .models import Users, Pitch, Comment
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from . import db



@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/signup')
def signup():
    
    return render_template('signup.html')

@app.route('/login')
def login():
    
    return render_template('login.html')

@app.route('/success')
def success():
    
    return render_template('success.html')

@app.route('/failure')
def failure():
    
    return render_template('failure.html')

@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html')

@app.route('/pitch')
def pitch():
    
    return render_template('pitch.html')

@app.route('/profile')
def profile():
    
    return render_template('profile.html')