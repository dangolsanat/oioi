from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    first_name=StringField("first Name")
    last_name = StringField("last Name")
    email = StringField("e-mail")
    user_image = StringField("image Link")
    dob = DateField("date of Birth")
    bio = StringField("your tagline")
    intro = TextAreaField("introduce yourself!")

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
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    neighbor = StringField('Neighbor', validators=[InputRequired()])
    borough = StringField('Borough', validators=[InputRequired()])
    images = FileField('Images', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')
                ], render_kw={"multiple": True})
    price = IntegerField('Price', validators=[InputRequired()])
    neighborhood = TextAreaField('Introduce your Neighborhood')
    submit = SubmitField('Add Post')
