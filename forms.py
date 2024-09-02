from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    first_name=StringField("first Name",render_kw={"class": "form-input"})
    last_name = StringField("last Name",render_kw={"class": "form-input"})
    email = StringField("e-mail",render_kw={"class": "form-input"})
    user_image = StringField("image Link",render_kw={"class": "form-input"})
    dob = DateField("date of Birth",render_kw={"class": "form-input"})
    bio = StringField("your tagline",render_kw={"class": "form-input"})
    intro = TextAreaField("introduce yourself!",render_kw={"class": "form-input"})

class LoginForm(FlaskForm):
    username = StringField(
        "Username", 
        validators=[InputRequired()],
        render_kw={"class": "form-input"}  # Add your desired class here
    )
    password = PasswordField(
        "Password", 
        validators=[InputRequired()],
        render_kw={"class": "form-input"}  # Add your desired class here
    )

class AddPost(FlaskForm):
    title = StringField('Title', validators=[InputRequired()],render_kw={"class": "form-input"})
    description = TextAreaField('Description', validators=[InputRequired()],render_kw={"class": "form-input"})
    address = StringField('Address', validators=[InputRequired()],render_kw={"class": "form-input"})
    neighbor = StringField('Neighbor', validators=[InputRequired()],render_kw={"class": "form-input"})
    borough = StringField('Borough', validators=[InputRequired()],render_kw={"class": "form-input"})
    images = FileField('Images', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')
                ], render_kw={"multiple": True})
    price = IntegerField('Price', validators=[InputRequired()],render_kw={"class": "form-input"})
    neighborhood = TextAreaField('Introduce your Neighborhood',render_kw={"class": "form-input"})
    submit = SubmitField('Add Post')
