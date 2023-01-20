from database import create_db_and_tables
from sqlmodel import Session, select
import hashlib
from controller.auth import validateLogin

from datetime import datetime, date



from database import engine
from models.forum_model import User, Post, SubPost
#from controller.users_controller import listAllUsers




def createUser():
    with Session(engine) as session:
        new_user = User(id=None,user_name=input("User name: "),name=input("Full name: "),password=hashlib.sha256(input("Password: ").encode('utf-8')).hexdigest())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(new_user)
        
def createPosts():
    with Session(engine) as session:
        #new_post = Post(id=None,date_created=TODAY,date_edited=TODAY, title=input("Event title: "), description=input("Event description: "), public=False, active=True, id_user=input("User ID: "),)
        new_post = Post(id=None, title=input("Event title: "), description=input("Event description: "), public=False, active=True, id_user=input("User ID: "),)
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
        print(new_post)


def createSubPosts():
    with Session(engine) as session:
        #new_post = Post(id=None,date_created=TODAY,date_edited=TODAY, title=input("Event title: "), description=input("Event description: "), public=False, active=True, id_user=input("User ID: "),)
        new_post = SubPost(id=None, description=input("Event description: "), id_post=input("Post ID: "), id_user=input("User ID: "),)
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
        print(new_post)





# test = validateLogin("jean", "123")

print(date.today())


### Uncoment to create Users
#createUser()

### Uncoment to create Events
#createPosts()

### Uncoment to create SubPosts
#createSubPosts()




### Finds a User and returns it with its respective Events
# with Session(engine) as session:
#     statement = select(User).where(User.user_name == "asd")
#     #statement = select(User)
#     user = session.exec(statement).first()
#     print("USER:")
#     print(user)
#     print("----POSTS----")
#     if user.posts:
#         for posts in user.posts:
#             print(posts)
            
#         print("----sub-posts----")
#         if user.sub_posts:
#             for sub_posts in user.sub_posts:
#                 print(sub_posts)


# with Session(engine) as session:
#     statement = select(User)
#     user = session.exec(statement).all()
    
    #print(user)
    
    # if user.events:
    #     for events in user.events:
    #         print(events)

# user = listAllUsers()

# for pessoa in user:
#     print(pessoa)
#     for evento in pessoa.events:
#         print(evento)



