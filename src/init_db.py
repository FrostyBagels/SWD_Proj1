'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import Course

# TODO
courses = [
    
]

with app.app_context():
    for prefix, number, name, credits in courses:
        pass
    print(f'Loaded {len(courses)} courses.')
