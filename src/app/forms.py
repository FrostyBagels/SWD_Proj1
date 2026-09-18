'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student:
Description: Homework 03 - Forms for the User Authentication Web App
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    about = TextAreaField('About')
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class LoginForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

GRADE_CHOICES = [
    'A+', 'A', 'A-',
    'B+', 'B', 'B-',
    'C+', 'C', 'C-',
    'D+', 'D', 'D-',
    'F'
]

class EnrollmentForm(FlaskForm):
    course = SelectField('Course', validators=[DataRequired()])
    grade = SelectField('Grade', choices=GRADE_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Confirm')

class DeleteEnrollmentForm(FlaskForm):
    submit = SubmitField('Delete')

