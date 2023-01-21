from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser, deleteUser
from controller.post_controller import createPost, createSubPost
from models.forms import FormCriarSubPost



@app.route('/posts/new_subpost/')
def new_subpost_form():

    form_criarsubpost = FormCriarSubPost()

    if session:
        if (session['user_logged_in'] == True):

            user_info = [session['ID'],session['user']]
            
            return render_template('form_new_subpost.html', user_info=user_info, form_criarsubpost = form_criarsubpost)
        else:
            return redirect(url_for('login'))
    else:
            return redirect('/login')



@app.route('/subposts/', methods=['GET', 'POST'])
def subpost():

    if request.method == 'GET':
        ### List all users 
        users_list = listUsers()
        print(users_list)
        return render_template('list_users.html', title = 'User list', users_list=users_list)
    elif request.method == 'POST':
        ### Create a new user on the database:
        if (request.form['description'] != ""):
        
            print(request.form['description'])
            createSubPost(session['ID'],request.form['description'])
            
            flash("SubPost Respondido.")
            
            return redirect(url_for("home"))
        else:
            flash("ERROR! Invalid parameters")
            
            return redirect(url_for("home"))