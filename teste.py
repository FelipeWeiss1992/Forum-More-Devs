import hashlib


jean = "teste"

cript = hashlib.sha256(jean.encode('utf-8')).hexdigest()
print(cript)





### List, update and delete a user based on ID and the post type
@app.route('/users/<id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def user_manager():

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
            if request.form['admin'] == "True":
                isAdmin = True
            updateUser(id, request.form['name'], isAdmin )
            flash(f"User {request.form['user_name']} altered.")

            return redirect(url_for("home"))
            
        case 'DELETE':
            ### Deletes a user by his ID
            pass
        case _:
            pass
        
        
# ####loop events list user
# <div class="events">
#         <p>Events:</p>
#         <ul>
#         {% for event in user.events %}
#             <li><h5>{{ event.title }}</h5> <p> {{ event.description }} </p> </li>
#         {% endfor %}
#         </ul>
#     </div>