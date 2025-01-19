from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Email, Length, URL, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserForm(FlaskForm):
    first_name = StringField("First Name", 
        validators=[InputRequired(), Length(max=25)],
        render_kw={"class": "form-input"})
    last_name = StringField("Last Name", 
        validators=[InputRequired(), Length(max=25)],
        render_kw={"class": "form-input"})
    email = StringField("Email", 
        validators=[InputRequired(), Email()],
        render_kw={"class": "form-input"})
    user_image = StringField("Image Link", 
        validators=[Optional(), URL()],
        render_kw={"class": "form-input"})
    dob = DateField("Date of Birth",
        validators=[InputRequired()],
        render_kw={"class": "form-input"})
    bio = StringField("Your Tagline",
        validators=[Optional(), Length(max=250)],
        render_kw={"class": "form-input"})
    intro = TextAreaField("Introduce Yourself!",
        validators=[Optional()],
        render_kw={"class": "form-input"})

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
    neighborhood = StringField('Neighborhood', validators=[InputRequired()],render_kw={"class": "form-input"})
    borough = StringField('Borough', validators=[InputRequired()],render_kw={"class": "form-input"})
    images = FileField('Images', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')
                ], render_kw={"multiple": True})
    price = IntegerField('Price', validators=[InputRequired()],render_kw={"class": "form-input"})
    neighborhood_description = TextAreaField('Introduce your Neighborhood',render_kw={"class": "form-input"})
    submit = SubmitField('Add Post')
