import pytest 
from gpa_calculator import calculate_gpa

def test_weighted_multi_course_average():
    enrollments = [
        {'grade': 'A', 'credits': 3},
        {'grade': 'B-', 'credits': 4},
    ]
    assert calculate_gpa(enrollments) == pytest.approx((4.0 * 3 + 2.7 * 4) / 7)

def test_single_course():
    assert calculate_gpa([{'grade': 'A-', 'credits': 3}]) == pytest.approx(3.7)

def test_empty_list_returns_zero():
    assert calculate_gpa([]) == 0

def test_ignores_upgraded_and_unrecognized_grades():
    enrollments = [
        {'grade': None, 'credits': 3},
        {'grade': 'Q', 'credits': 4},
        {'grade': 'A', 'credits': 3},
    ]
    assert calculate_gpa(enrollments) == pytest.approx(4.0)