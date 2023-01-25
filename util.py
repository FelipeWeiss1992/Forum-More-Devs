from database import create_db_and_tables
from sqlmodel import Session, select
import hashlib
from controller.auth import validateLogin
#from controller.users_controller import listUsers
#from controller.post_controller import deletePost
from datetime import datetime, date

from sqlalchemy.orm import selectinload, joinedload



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


def listReplyOfPost(postID):
    with Session(engine) as session:
        statement = select(SubPost).where(SubPost.id_post == postID)
        posts_rep = session.exec(statement).all()
        print(posts_rep)
    
### Delete a post based on its ID and Sub Posts if also has it
def deletePost(postID, userID=None):
    with Session(engine) as session:
        statement = select(Post).where(Post.id == postID).options(selectinload(Post.sub_posts))
        post_rep = session.exec(statement).first()
        if post_rep != None:
            session.delete(post_rep)
            session.commit()
            if post_rep.sub_posts:
                for subposts in post_rep.sub_posts:
                    print("subs")
                    print(subposts)
                    deleteSubPost(1, postID, subposts.id)
            print("apagou main post")
            return True
        else:
            print("Não achou nada")
            return False
        
        
### Delete sub posts based on its ID
def deleteSubPost(subPostID, userID=None, postID=None):
    with Session(engine) as session:
        statement = select(SubPost).where(SubPost.id == subPostID)
        post_rep = session.exec(statement).first()
        if post_rep != None:
            session.delete(post_rep)
            session.commit()
            print("apagou")
            return "APAGOU"
        else:
            print("Não achou nada")
            return False
    

# test = validateLogin("jean", "123")

print(date.today())


### Uncoment to create Users
#createUser()

### Uncoment to create Events
#createPosts()

### Uncoment to create SubPosts
#createSubPosts()


#listReplyOfPost(3)


### Finds a User and returns it with its respective Events
# with Session(engine) as session:
#     statement = select(User).where(User.user_name == "jean")
#     #statement = select(User)
#     user = session.exec(statement).first()
    # print("USER:")
    # print(user)
    # print("----POSTS----")
    # if user.posts:
    #     for posts in user.posts:
    #         print(posts)
        
    #     print("----sub-posts----")
    #     if user.sub_posts:
    #         for sub_posts in user.sub_posts:
    #             print(sub_posts)


# with Session(engine) as session:
#     statement = select(User)
#     user = session.exec(statement).all()
    
#     print(user)
    
#     if user.events:
#         for events in user.events:
#             print(events)

# user = listUsers()

# for pessoa in user:
#     print("PESSOA")
#     print(pessoa)

#     print("EVENTOS: ")
#     if pessoa.sub_posts:
#         for evento in pessoa.sub_posts:
#             print(f"  Evento: {evento}")


deletePost(9)
#deleteSubPost(8)