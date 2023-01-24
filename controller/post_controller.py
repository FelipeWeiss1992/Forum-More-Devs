from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from main import app

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

def createSubPost(userID, postID,subpost_description):
    with Session(engine) as session:
        new_subpost = SubPost(id=None, description=subpost_description, id_post=postID, id_user=userID)
        session.add(new_subpost)
        session.commit()
        session.refresh(new_subpost)
        print(new_subpost)
        return True
        
def listReplyOfPost(postID):
    with Session(engine) as session:
        statement = select(SubPost).where(SubPost.id_post == postID)
        posts_rep = session.exec(statement).all()
        return posts_rep
    
#### Testando possibilidade de uso de funcioções dentro do jinja para poder retornar a quantidade de posts (ainda precisa ajustar)
@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)