from database import create_db_and_tables
from sqlmodel import Session, select
import hashlib
from controller.auth import validateLogin


from database import engine
from models.calendar_model import User, Event
#from controller.users_controller import listAllUsers

def createUser():
    with Session(engine) as session:
        new_user = User(id=None,user_name=input("User name: "),name=input("Full name: "),password=hashlib.sha256(input("Password: ").encode('utf-8')).hexdigest())
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(new_user)
        
def createEvents():
    with Session(engine) as session:
        new_event = Event(id=None,data_event=input("Event date: "), title=input("Event title: "), description=input("Event description: "), public=False, active=True, id_user=input("User ID: "),)
        session.add(new_event)
        session.commit()
        session.refresh(new_event)
        print(new_event)



test = validateLogin("jean", "123")

print(test)


### Uncoment to create Users
#createUser()

### Uncoment to create Events
#createEvents()

### Finds a User and returns it with its respective Events
# with Session(engine) as session:
#     statement = select(User).where(User.user_name == "jean")
#     #statement = select(User)
#     user = session.exec(statement).first()
    
#     print(user)
    
#     if user.events:
#         for events in user.events:
#             print(events)



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


createEvents()
