from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser, deleteUser
from controller.post_controller import createPost
from models.forms import FormCriarPost



@app.route('/posts/new_post/')
def new_post_form():

    form_criarpost = FormCriarPost()

    if session:
        if (session['user_logged_in'] == True):

            user_info = [session['ID'],session['user']]
            
            return render_template('form_new_post.html', user_info=user_info, form_criarpost = form_criarpost)
        else:
            return redirect(url_for('login'))
    else:
            return redirect('/login')



@app.route('/posts/', methods=['GET', 'POST'])
def post():

    if request.method == 'GET':
        ### List all users 
        users_list = listUsers()
        print(users_list)
        return render_template('list_users.html', title = 'User list', users_list=users_list)
    elif request.method == 'POST':
        ### Create a new user on the database:
        if (request.form['title'] != "") and (request.form['description'] != ""):
        
            print(request.form['title'], request.form['description'])
            createPost(session['ID'], request.form['title'],request.form['description'])
            
            flash("Post created.")
            
            return redirect(url_for("home"))
        else:
            flash("ERROR! Invalid parameters")
            
            return redirect(url_for("home"))