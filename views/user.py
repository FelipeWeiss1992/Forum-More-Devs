from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser, deleteUser

###
### User manupulation
###

###
### List all users or create a new user based on the post type:
@app.route('/users/', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        ### List all users 
        users_list = listUsers()
        print(users_list)
        return render_template('list_users.html', title = 'User list', users_list=users_list)
    elif request.method == 'POST':
        ### Create a new user on the database:
        if (request.form['user_name'] != "") and (request.form['name'] != "") and (request.form['password1'] != ""):
        
            print(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
            createUser(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
            
            flash(f"User {request.form['user_name']} created.")
            
            return redirect(url_for("home"))
        else:
            flash("ERROR! Invalid parameters")
            
            return redirect(url_for("home"))


### List, update and delete a user based on ID and the post type
@app.route('/users/<id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def user_manager(id):

    match request.method:
        case 'GET':
            ### List user by ID
            users_list = listUsers(id)
            print(users_list)
            return render_template('list_single_user.html', title = 'User list', user=users_list)
        case 'POST':
            pass
        case 'PATCH':
            ### Edit a user by his ID
            isAdmin = False
            #Verify if the new user has the Admin selected and convert it to a proper bolean type.
            if request.form['admin'] == "True":
                isAdmin = True
            updateUser(id, request.form['name'], isAdmin )
            #flash(f"User {request.form['user_name']} altered.")

            return redirect(url_for("home")), 200
            
        case 'DELETE':
            ### Deletes a user by his ID
            deleteUser(id)
            flash("Usuário deletado")

            #return redirect(url_for("home"))
            return "APAGOU!"
            
        case _:
            pass
        

### FORMS to manipulate users
###
### Return a FORM to edit a specific user based on his ID
@app.get('/users/edit/<id>/')
def editUserForm(id):
    users_list = listUsers(id)
    print(users_list)
    return render_template('edit_user.html', title = 'Edit user: ' + users_list.name, user=users_list)

### FORM to add new users
@app.route('/users/new_user')
def new_user_form():
    if session:
        if (session['user_logged_in'] == True):

            user_info = [session['ID'],session['user']]

            return render_template('form_new_user.html', user_info=user_info)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

    
### End of User routes