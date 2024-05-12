from __future__ import annotations
from datetime import datetime
import json
from typing import Type
from sqlalchemy import inspect
from .. import db


class Base(db.Model):
    """
    Base model
    """
    __abstract__ = True
    __tablename__ = "base"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    # def __init__(self,
    #              created_at: datetime = datetime.now(),
    #              updated_at: datetime = datetime.now()):
    #     self.created_at = created_at
    #     self.updated_at = updated_at

   
    # This must be overridden by derived classes
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
