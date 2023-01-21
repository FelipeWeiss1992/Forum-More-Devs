from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from models.forum_model import User, Post, SubPost


from database import engine


def createPost(userID, post_title, post_description):
    with Session(engine) as session:
        new_post = Post(id=None, title=post_title, description=post_description, public=False, active=True, id_user=userID)
        session.add(new_post)
        session.commit()
        session.refresh(new_post)
        print(new_post)


def listPost(userID):
    pass

def editPost(userID,id):
    pass

def deletePost(userID, id):
    pass



def createSubPost(userID,subpost_description):
    with Session(engine) as session:
        new_subpost = SubPost(id=None, description=subpost_description, id_post="2", id_user=userID)
        session.add(new_subpost)
        session.commit()
        session.refresh(new_subpost)
        print(new_subpost)