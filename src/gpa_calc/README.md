# CS3250 - Project 1: GPA Calculator

Computes credit-weighted GPA on a 4.3 scale from a list of course dictionaries.

## Usage

```python
courses = [
    {'credits': 4, 'grade': 'A'},
    {'credits': 3, 'grade': 'B+'},
]

print(calculate_gpa(courses))
