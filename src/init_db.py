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
    ('CS', '3250', 'Software Development Methods and Tools', 4),
    ('CS', '2240', 'Discrete Structures', 4),
    ( 'MTH', '3210', 'Probability and Statistics', 4),
    ('THE', '2295', 'Comedy: In-Print and On-Stage', 3),
    ('MTH', '3130', 'Linear Algebra', 4)
]

with app.app_context():
    for prefix, number, name, credits in courses:
        pass
    print(f'Loaded {len(courses)} courses.')
