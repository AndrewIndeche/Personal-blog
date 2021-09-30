from . import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user,UserMixin
from datetime import datetime

class Quote():
    def __init__(self,user,id,quote,permalink):
        self.user = user
        self.id = id
        self.quote= quote
        self.permalink = permalink


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_encrypt=db.Column(db.String(128))
    quotes = db.relationship('quotes', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')

    @property   #write-only
    def password(self):
        raise AttributeError('You can only read this attribute')

    @password.setter
    def password(self, password):
        self.password_encrypt = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_encrypt, password)

    def __repr__(self):
        return f'User{self.username}'


class Quotes(db.Model):
    __tablename__='quotes'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comments', backref='quote', lazy='dynamic')

    def save_quote(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Quotes{self.text}'


class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,quote_id):
        comments = Comments.query.filter_by(quote_id=quote_id)
        return comments

    def __repr__(self):
        return f'Comments:{self.comment}'
