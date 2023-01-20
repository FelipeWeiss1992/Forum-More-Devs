from sqlmodel import Session, select
from sqlalchemy.orm import selectinload

from models.calendar_model import User, Event

from database import engine


def createEvent(userID):
    pass

def listEvents(userID):
    pass

def editEvent(userID,id):
    pass

def deleteEvent(userID, id):
    pass

