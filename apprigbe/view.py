from flask import render_template
from apprigbe import app

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/work')

def work():
    return render_template('work.html')

@app.route('/code')

def code():
    return render_template('code.html')

@app.route('/contact')

def contact():
    return render_template('contact.html')

