from datetime import datetime, date
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    user_name: str = Field(index=True)
    name: str = Field(index=True)
    admin: bool = Field(nullable=True)
    password: str = Field(nullable=False)
    suspended: bool = Field(default=False, nullable=False, index=True)

    posts: List["Post"] = Relationship(back_populates="users")
    sub_posts: List["SubPost"] = Relationship(back_populates="users")


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    date_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    title: str = Field(nullable=False, index=True)
    description: str = Field()
    public: bool = Field(default=False)
    active: bool = Field(default=True)
    
    id_user: Optional[int] = Field(default=None, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="posts")
    
    sub_posts: Optional[List["SubPost"]] = Relationship(back_populates="posts")
    

# class SubPost(Post, table=True):
#     id_post: Optional[int] = Field(default=None, foreign_key="post.id")
#     posts: Optional[Post] = Relationship(back_populates="sub_posts")
    
    
    
class SubPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    date_edited: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    description: str = Field()
    
    id_user: Optional[int] = Field(default=None, foreign_key="user.id")
    users: Optional[User] = Relationship(back_populates="sub_posts")
    
    id_post: Optional[int] = Field(default=None, foreign_key="post.id")
    posts: Optional[Post] = Relationship(back_populates="sub_posts")