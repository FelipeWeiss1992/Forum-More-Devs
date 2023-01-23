from sqlmodel import Session, select
from sqlalchemy.orm import selectinload, joinedload
import hashlib

from models.forum_model import User, Post, SubPost

from database import engine


### Select a user by its ID or user name if none has been passed it will return all users
# Should NOT be used with both parameters at the same time.
def listUsers(id=None):
    with Session(engine) as session:
        ### The option .options(selectinload(User.events)) has to me used so that the query returns the data instead o "lazy loading" it
        ### if removed the option, you will have to use de data only inside of a session otherwise an error will be trown as lazy load problem.
        if id != None:
            statement = select(User).where(User.id == id).options(selectinload(User.posts)).options(selectinload(User.sub_posts))
            user = session.exec(statement).first()
            print(user)
            return user
        
        else:
            #statement = select(User).options(selectinload(User.posts))
            #statement = select(User).options(selectinload(User.posts)).options(selectinload(User.sub_posts))
            statement = select(User).options(selectinload(User.posts),selectinload(User.sub_posts) )
            user = session.exec(statement)
            ### The .all() is used to return the result as an Object, otherwise the return will be shown as a object in the memory. The .first() also can be used to return a single object.
            return user.all()
    
def createUser(user_name, name, password, admin=False):
    if admin == "True":
        admin = True
    else:
        admin = False
        
    with Session(engine) as session:
        new_user = User(id=None,user_name=user_name,name=name,password=hashlib.sha256(password.encode('utf-8')).hexdigest(), admin=admin)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(new_user)
        
def updateUser(id, name, admin=False):
    with Session(engine) as session:
        user = listUsers(id)

        user.name = name
        user.admin = admin
                
        session.add(user)
        session.commit()
        session.refresh(user)
        print("Updated hero:", user)
        
        return "teste feito"
    
def deleteUser(id):
    with Session(engine) as session:
        user = listUsers(id)
        #If has a user to delete:
        #if user:
        session.delete(user)
        session.commit()
        return "APAGOU"