from flask import render_template, request, redirect, session, flash, url_for
from main import app
#from controller.users_controller import listUsers, createUser, updateUser
from controller.auth import validateLogin
import calendar
from datetime import date
from models.forms import FormLogin


###
### Home route
### Checks if the user is logged in and then list the calendar, otherwise send it back to login screen

@app.route('/')
def home():
    if session:
        if (session['user_logged_in'] == True):
       # if 'teste' == 'teste1':
            user_info = [session['ID'],session['user']]
            #return render_template('calendar.html',  aux=0)
            return render_template('calendar.html',user_info=user_info)
        else:
            return redirect(url_for('login'))
    else:
        return redirect('/login')


@app.route('/new_event/', methods=['POST'])
def new_event():
    pass

### End of Home route


###
### Login and Authenticate routes
###

@app.route('/login/')
def login():
    form_login = FormLogin()
    
    return render_template('login.html', titulo = 'User login', form_login = form_login)

@app.route('/autenticate', methods=['POST',])
def autenticate():
    autenticated, user_auth = validateLogin(request.form['user_name'], request.form['password'])
    
    if autenticated:
        session['user_logged_in'] = True
        session['user'] = user_auth.user_name
        session['ID'] = user_auth.id
        
        flash('Successfully logged in')

        return redirect(url_for("home"))
    else:
        flash('Invalid credentials')
        return redirect(url_for("login"))

@app.route('/logout/')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

#### End of Login routes

