'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s): Cameron Greeson, Pete Dives, Steph Rivera, Tyler Black,
Description: Project 1 - GPA Calculator
'''
from flask_sqlalchemy import SQLAlchemy

from app.models import Course

COURSES = [
    ('CS', '3250', 'Software Development Methods and Tools', 4),
    ('CS', '2240', 'Discrete Structures', 4),
    ('MTH', '3210', 'Probability and Statistics', 4),
    ('THE', '2295', 'Comedy: In-Print and On-Stage', 3),
    ('MTH', '3130', 'Linear Algebra', 4),
    ('CS', '3600', 'Operating Systems', 4),
    ('CS', '4050', 'Algorithms and Algorithm Analysis', 4),
    ('BVG', '4000', 'Applied Brewing Operations', 3),
    ('PHI', '3370', 'Computers, Ethics, and Society', 3),
    ('JMP', '2610', 'Introduction to Technical Writing', 3),
    ('BIO', '1080', 'General Biology I', 3),
    ('NUT', '2040', 'Introduction to Nutrition', 3),
    ('CAS', '1010', 'Public Speaking', 3),
    ('MTH', '1410', 'Calculus I', 4),
]

def seed_db(db: SQLAlchemy):
    """
    Seeds the database with the courses listed in COURSES above.

    :param db: SQLAlchemy database object.
    """
    for prefix, num, name, creds in COURSES:
        course = Course(prefix=prefix, number=num, name=name, credits=creds)
        db.session.add(course)
    db.session.commit()

    print(f'Loaded {len(COURSES)} courses.')
