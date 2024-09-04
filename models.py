from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask import current_app as app


db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # Relationships
    full_user = db.relationship('Full_user', uselist=False, back_populates='user')
    sent_messages = db.relationship('Message', foreign_keys='Message.sender_id', back_populates='sender')
    received_messages = db.relationship('Message', foreign_keys='Message.receiver_id', back_populates='receiver')

    @classmethod
    def register(cls, username, pwd):
        """Register user with hashed password & return user."""
        hashed = bcrypt.generate_password_hash(pwd).decode('utf-8')
        return cls(username=username, password=hashed)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct."""
        user = cls.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        else:
            return False

class Full_user(db.Model):
    __tablename__ = 'full_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    user_image = db.Column(db.Text, nullable=True)
    dob = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String(250), nullable=True)
    intro = db.Column(db.Text, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    # Relationships
    user = db.relationship('Users', back_populates='full_user')
 

    @classmethod
    def add_profile(cls, user_id, firstname, lastname, email, image, dob, bio, intro):
        new_user = cls(
            first_name=firstname,
            last_name=lastname,
            email=email,
            user_image=image,
            dob=dob,
            bio=bio,
            intro=intro,    
            user_id=user_id
        )
        db.session.add(new_user)
        db.session.commit()

    def calculate_age(self):
        today = datetime.today().date()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    # Relationships
    sender = db.relationship('Users', foreign_keys=[sender_id], back_populates='sent_messages')
    receiver = db.relationship('Users', foreign_keys=[receiver_id], back_populates='received_messages')

    @classmethod
    def send_message(cls, sender_id, receiver_id, content):
        """Send a message from one user to another."""
        message = cls(sender_id=sender_id, receiver_id=receiver_id, content=content)
        db.session.add(message)
        db.session.commit()
        return message



class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    neighbor = db.Column(db.String(50), nullable=False)
    borough = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    neighborhood = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    user_rel = db.relationship('Users', backref=db.backref('posts', lazy=True))

    @classmethod
    def add_post(cls, user_id, title, description, address, neighbor,price, borough, neighborhood):
        try:
            post = cls(
                title=title,
                description=description,
                address=address,
                neighbor=neighbor,
                borough=borough,
                price=price,
                neighborhood=neighborhood,
                user_id=user_id,
            )
            db.session.add(post)
            db.session.commit()
            return post
        except Exception as e:
            print(f"Error adding post: {e}")
            db.session.rollback()
            return None

class PostImage(db.Model):
    __tablename__ = 'post_images'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(1000), nullable=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    # Relationships
    post_rel = db.relationship('Post', backref=db.backref('images', lazy=True))

    @classmethod
    def add_image(cls, post_id, url):
        try:
            image_instance = cls(post_id=post_id, url=url)
            db.session.add(image_instance)
            db.session.commit()
            return image_instance
        except Exception as e:
            print(f"Error adding image: {e}")
            db.session.rollback()
            return None