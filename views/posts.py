from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser, deleteUser
from controller.post_controller import createPost, createSubPost
from models.forms import FormCriarPost
#from views.views import home



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
        ### Create a post on the database:
        
        if session:
            if (session['user_logged_in'] == True):

                user_info = [session['ID'],session['user']]
                
                createPost(session['ID'], request.form['title'],request.form['description'])
                
                flash("Post created.")
                
                return redirect(url_for("home"))
                
            else:
                return redirect(url_for('login'))
        else:
                return redirect(url_for('login'))

        
@app.post('/posts/<id>/new_subpost/')
def new_subpost(id):

    if session:
        if (session['user_logged_in'] == True):

            user_info = [session['ID'],session['user']]
            
            createSubPost(session['ID'], id, request.form['description'])
            
            return redirect(url_for("home"))

        else:
            return redirect(url_for('login'))
    else:
            return redirect('/login')