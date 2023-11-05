from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
import os
from flask import request
from werkzeug.utils import secure_filename

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class VideoUploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    video = FileField('Video', validators=[DataRequired()])
    submit = SubmitField('Upload')

    def save_video(self):
         if 'video' in request.files:
            video_file = request.files['video']
            if video_file:
                video_path = os.path.join(os.path.abspath("static/videos") , self.title.data+'.mp4')
                print("Reached till here: ", video_path)
                os.makedirs(os.path.dirname(video_path), exist_ok=True)
                video_file.save(video_path)
                print("Saving was success")
                return video_path