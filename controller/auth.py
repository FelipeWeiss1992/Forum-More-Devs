import hashlib
from sqlmodel import Session, select
#from sqlalchemy.orm import selectinload

from models.calendar_model import User, Event

from database import engine

def validateLogin(user, password):

    with Session(engine) as session:
        ### The option .options(selectinload(User.events)) has to me used so that the query returns the data instead o "lazy loading" it
        ### if removed the option, you will have to use de data only inside of a session otherwise an error will be trown as lazy load problem.
        statement = select(User).where(User.user_name == user)
        user_db = session.exec(statement).first()
        ### The .all() is used to return the result as an Object, otherwise the return will be shown as a object in the memory. The .first() also can be used to return a single object.
        #return user.all()

        if user_db is not None:
            if user == user_db.user_name and user_db.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                print("User logged in")
                return True, user_db
            else:
                print("User or password dont match")
                return False

            
        else:
            print("User not found")
            return False
