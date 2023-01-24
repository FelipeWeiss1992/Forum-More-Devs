from flask import render_template, request, redirect, session, flash, url_for
from main import app
from controller.users_controller import listUsers, createUser, updateUser, deleteUser
from models.forms import FormCriarConta

###
### User manupulation
###

###
### List all users or create a new user based on the post type:
@app.route('/users/', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        ### List all users 
        if (session['user_logged_in'] == True):
            user_info = [session['ID'],session['user']]
            users_list = listUsers()
            print(users_list)
            return render_template('list_users.html',users_list=users_list, user_info=user_info)
    elif request.method == 'POST':
        ### Create a new user on the database:
        user_info = [session['ID'],session['user']]
        
        if (request.form['user_name'] != "") and (request.form['name'] != "") and (request.form['password1'] != ""):
        
            print(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
            createUser(request.form['user_name'], request.form['name'],request.form['password1'],request.form['admin'])
            
            flash(f"User {request.form['user_name']} created.")
            
            return redirect(url_for("home"), user_info=user_info)
        else:
            flash("ERROR! Invalid parameters")
            
            return redirect(url_for("home"))
    else:
        return redirect(url_for('login'))


### List, update and delete a user based on ID and the post type
@app.route('/users/<id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def user_manager(id):

    match request.method:
        case 'GET':
            ### List user by ID
            if (session['user_logged_in'] == True):
                user_info = [session['ID'],session['user']]
                users_list = listUsers()
                print(users_list)
                users_list = listUsers(id)
                print(users_list)
                return render_template('list_single_user.html', title = 'User list', user=users_list, user_info=user_info)
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
    user_info = [session['ID'],session['user']]
    
    print(users_list)
    return render_template('edit_user.html', title = 'Edit user: ' + users_list.name, user=users_list, user_info=user_info)

### FORM to add new users
@app.route('/users/new_user')
def new_user_form():

    form_criar_conta = FormCriarConta()

    return render_template('form_new_user.html', form_criarconta = form_criar_conta)


    
### End of User routes