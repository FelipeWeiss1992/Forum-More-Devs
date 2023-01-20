from flask import render_template, request, redirect, session, flash, url_for
from main import app
#from controller.users_controller import listUsers, createUser, updateUser
from controller.auth import validateLogin
import calendar
from datetime import date


###
### Home route
### Checks if the user is logged in and then list the calendar, otherwise send it back to login screen

@app.route('/')
def home():
    if session:
        if (session['user_logged_in'] == True):
            currentDate = date.today()
            cal = calendar.Calendar(firstweekday=6)
            DIAS_DA_SEMANA = ("SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY")
            calDays = cal.monthdayscalendar(2022, 12)
            user_info = [session['ID'],session['user']]

            return render_template('calendar.html', calDays=calDays, aux=0, DIAS_DA_SEMANA=DIAS_DA_SEMANA, user_info=user_info, title=currentDate)
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
    return render_template('login.html', titulo = 'User login')

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

