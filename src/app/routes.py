'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student: 
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import User, Course, Enrollment
from app.forms import SignUpForm, LoginForm, EnrollmentForm, DeleteEnrollmentForm, UpdateGradeForm
from gpa_calculator import calculate_gpa
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
    return "Work in progress..."
    
# TODO: from hwk-3
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    return "Work in progress..."

# TODO: from hwk-3
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    return "Work in progress..."

# TODO
@app.route('/enrollments')
@login_required
def list_enrollments():
    enrollments = current_user.enrollments
    gpa = calculate_gpa([{'grade': e.grade, 'credits': e.course.credits} for e in enrollments if e.grade])
    delete_form = DeleteEnrollmentForm()
    update_form = UpdateGradeForm()
    return render_template('enrollments.html', enrollments=enrollments, gpa=gpa, delete_form=delete_form, update_form=update_form)

# TODO
@app.route('/enrollments/delete/<course_prefix>/<course_number>', methods=['POST'])
@login_required
def delete_enrollment(course_prefix, course_number):
    form = DeleteEnrollmentForm()
    if form.validate_on_submit():
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
    form.course.choices = [f'{c.prefix} {c.number}' for c in Course.query.all()]
    if form.validate_on_submit():
        prefix, number = form.course.data.split(' ', 1)
        existing = Enrollment.query.filter_by(user_id=current_user.id, course_prefix=prefix, course_number=number).first()
        if existing:
            form.course.errors.append('You have already enrolled in this course. Update your grade from the enrollments list instead')
        else:
            db.session.add(Enrollment(user_id=current_user.id, course_prefix=prefix, course_number=number, grade=form.grade.data))
            db.session.commit()
            return redirect(url_for('list_enrollments'))
    return render_template('create_enrollment.html', form=form)

@app.route('/enrollments/update/<course_prefix>/<course_number>', methods=['POST'])
@login_required
def update_enrollment(course_prefix, course_number):
    form = UpdateGradeForm()
    if form.validate_on_submit():
        enrollment = Enrollment.query.filter_by(user_id=current_user.id, course_prefix=course_prefix, course_number=course_number).first()
        if enrollment:
            enrollment.grade = form.grade.data
            db.session.commit()
    return redirect(url_for('list_enrollments'))
