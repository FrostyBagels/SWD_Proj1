'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student: 
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import User, Course, Enrollment
from app.forms import SignUpForm, LoginForm, EnrollmentForm, DeleteEnrollmentForm
# TODO
# from gpa_calculator_xx import calculate_gpa
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

# TODO: from hwk-3
@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        if form.passwd.data != form.passwd_confirm.data:
            return render_template('signup.html', form=form, error='Passwords do not match.')
        
        existing_user = User.query.filter_by(id=form.id.data).first()

        if existing_user:
             return render_template('signup.html', form=form, error='User already exists.')

    hashed = bcrypt.hashpw(form.passwd.data.encode('utf-8'), bcrypt.gensalt())
    user = User(id=form.id.data, name=form.name.data, about=form.about.data, passwd=hashed)
    db.session.add(user)
    db.session.commit()

    return "Work in progress..."
    
# TODO: from hwk-3
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()

        if user and bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html', form=form, error='Invalid username or password.')

    return render_template('login.html', form=form)

# TODO: from hwk-3
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('index'))

# TODO
@app.route('/enrollments')
@login_required
def list_enrollments():
    enrollments = Enrollment.query.filter_by(user_id=current_user.id).all()

    return render_template('enrollments.html', enrollments=enrollments)

# TODO
@app.route('/enrollments/delete/<course_prefix>/<course_number>', methods=['POST'])
@login_required
def delete_enrollment(course_prefix, course_number):
    enrollment = Enrollment.query.filter_by(user_id=current_user.id, course_prefix=course_prefix, course_number=course_number).first()

    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()

    return redirect(url_for('list_enrollments'))
# TODO
@app.route('/enrollments/create', methods=['GET', 'POST'])
@login_required
def create_enrollment():

    form = EnrollmentForm()

    courses = Course.query.all()

    choices = []

    for course in courses:
        choices.append(
            (course.prefix + "-" + course.number,
             course.prefix + " " + course.number)
        )

    form.course.choices = choices

    if form.validate_on_submit():
        course_prefix, course_number = form.course.data.split("-")
        enrollement = Enrollment(user_id=current_user.id, course_prefix=course_prefix, course_number=course_number, grade=form.grade.data)
        db.session.add(enrollement)
        db.session.commit()
    