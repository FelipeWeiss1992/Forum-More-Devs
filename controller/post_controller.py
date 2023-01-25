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


def listPost(postID, userID=None):
    with Session(engine) as session:
        statement = select(Post).where(Post.id == postID)
        post_rep = session.exec(statement).first()
        if post_rep != None:
            return post_rep
        else:
            return False

def editPost(postID, postTitle, postDescription, userID=None):
    with Session(engine) as session:
        statement = select(Post).where(Post.id == postID)
        post_rep = session.exec(statement).first()
        if post_rep != None:
            post_rep.title = postTitle
            post_rep.description = postDescription
            
            session.add(post_rep)
            session.commit()
            session.refresh(post_rep)
        else:
            return False

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
                    print(subposts)
                    deleteSubPost(1, postID, subposts.id)
            return True
        else:
            return False
        
### Delete sub posts based on its ID
def deleteSubPost(subPostID, userID=None, postID=None):
    with Session(engine) as session:
        statement = select(SubPost).where(SubPost.id == subPostID)
        post_rep = session.exec(statement).first()
        if post_rep != None:
            session.delete(post_rep)
            session.commit()
            return True
        else:
            return False

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