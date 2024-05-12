from __future__ import annotations
from .base import Base
from .. import db

class Chat(Base):
    __tablename__ = "chat_table"
    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name = db.mapped_column(db.String(50), nullable=False)
    messages = db.relationship("Message",back_populates="chat",uselist=True)
    def __repr__(self):
        return f"<Chat: {self.name} >"


class Message(Base):
    __tablename__ = "message_table"
    id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    content = db.mapped_column(db.String(), nullable=False)
    senderName = db.mapped_column(db.String(50), nullable=False)
    chat_id = db.mapped_column(db.Integer, db.ForeignKey('chat_table.id',ondelete="CASCADE"),nullable=False,index=True)
    # chat = db.relationship('Chat',backref=db.backref('message',lazy=True))
    chat = db.relationship("Chat",back_populates="messages")
    def __repr__(self):
        return f"<Message: {self.content} \n from:{self.senderName}  >"
    

# cascade , backref, back_populates, lazy

"""
backref, back_populates:
creates a bidirectional relationship that will automatically allow SQLAlchemy to 
recognize that there is a connection between two instances.

ex: once u create children they will be assigned to parent directly 

-backref 
With backref you only need to declare the relationship in one class (parent)
and forieignkey in the other one (child)

# parent
children = db.relationship("Child", backref="parent") 

# child
parent_id = db.mapped_column(db.Integer, db.ForeignKey("parents.id"))


-back_populates
When using back_populates you must explicitly create the relationship in both the parent and child classes:

children = db.relationship("Child", back_populates="parent") 
parent = db.relationship("Child", back_populates="children")
"""