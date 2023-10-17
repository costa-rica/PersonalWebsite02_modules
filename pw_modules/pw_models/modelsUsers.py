from .main import dict_base, dict_sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table, JSON

from itsdangerous.url_safe import URLSafeTimedSerializer#new 2023
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app

Base_users = dict_base['Base_users']
sess_users = dict_sess['sess_users']

def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]



class Users(Base_users, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    permissions = Column(Text)
    posts = relationship('BlogPosts', backref='author', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, permissions: {self.permissions})'


class BlogPosts(Base_users):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id_name_string = Column(Text)
    network_post_id = Column(Text)
    title = Column(Text)
    description = Column(Text)
    edited = Column(Text)
    post_html_filename = Column(Text)
    word_doc_to_html_filename = Column(Text)
    images_dir_name = Column(Text)
    notes = Column(JSON)
    tags = Column(JSON)
    icon_file = Column(Text)
    url = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)


    def __repr__(self):
        return f'BlogPosts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'
