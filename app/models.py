from typing import List

from sqlalchemy.orm import Mapped, relationship
from app import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import LONGTEXT


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    password: Mapped[str] = Column(String(2048))
    username: Mapped[str] = Column(String(256))
    type: Mapped[str] = Column(String(256))

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "type",
    }


class Admin(User):
    __tablename__ = 'admin'
    id: Mapped[int] = Column(Integer, ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True,
                             autoincrement=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }


class Student(User):
    __tablename__ = 'student'
    id: Mapped[int] = Column(Integer, ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'),
                             primary_key=True, autoincrement=True)
    topics: Mapped[List["Topic"]] = db.relationship(secondary='assigned_table')

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }


class Logs(db.Model):
    __tablename__ = 'logs'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = Column(Integer, )
    student: Mapped["Student"] = db.relationship('Student')
    prompt: Mapped[str] = Column(LONGTEXT)
    response: Mapped[str] = Column(LONGTEXT)


class Topic(db.Model):
    __tablename__ = 'topic'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String(2048))
    text: Mapped[str] = Column(LONGTEXT)


class Question(db.Model):
    __tablename__ = 'question'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = Column(LONGTEXT)
    answer: Mapped[str] = Column(String(2048))
    topic_id: Mapped[int] = Column(Integer, ForeignKey('topic.id', onupdate='CASCADE', ondelete='CASCADE'))
    topic: Mapped["Topic"] = db.relationship('Topic')


assigned_table = db.Table(
    'assigned_table',
    db.Model.metadata,
    Column('student_id', ForeignKey('student.id', ondelete='CASCADE', onupdate='CASCADE')),
    Column('topic_id', ForeignKey('topic.id', ondelete='CASCADE', onupdate='CASCADE')),
)



