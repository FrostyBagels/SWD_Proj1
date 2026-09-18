'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

from app import db
from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy

# grade points for the traditional college letter grade scale, A+ included (so GPA can exceed 4.0)
GRADE_POINTS = {
    'A+': 4.3, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'D-': 0.7,
    'F': 0.0
}

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)
    enrollments = db.relationship('Enrollment', back_populates='user')
    courses = association_proxy('enrollments', 'course')

class Course(db.Model):
    __tablename__ = 'courses'
    prefix = db.Column(db.String, primary_key=True)
    number = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    credits = db.Column(db.Integer)
    enrollments = db.relationship('Enrollment', back_populates='course')
    students = association_proxy('enrollments', 'user')

# association object linking a user to a course, with the grade earned
class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    user_id = db.Column(db.String, db.ForeignKey('users.id'), primary_key=True)
    course_prefix = db.Column(db.String, primary_key=True)
    course_number = db.Column(db.String, primary_key=True)
    grade = db.Column(db.String)
    __table_args__ = (
        db.ForeignKeyConstraint(['course_prefix', 'course_number'], ['courses.prefix', 'courses.number']),
    )
    user = db.relationship('User', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')


