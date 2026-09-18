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
    return "Work in progress..."

# TODO
@app.route('/enrollments/delete/<course_prefix>/<course_number>', methods=['POST'])
@login_required
def delete_enrollment(course_prefix, course_number):
    return "Work in progress..."

# TODO
@app.route('/enrollments/create', methods=['GET', 'POST'])
@login_required
def create_enrollment():
    return "Work in progress..."