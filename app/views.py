from flask import render_template
from app import app



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