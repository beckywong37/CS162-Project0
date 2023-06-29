# Author: Becky Wong
# GitHub username: beckywong37
# Date: 06/27/223
# Description: Defines a Student class that represents a student with a name and grade, with a method to
# retrieve grade. The student_stats function outside the class takes a list of Student objects and returns the
# mean, median, and mode in a tuple format.

import statistics


class Student:
    """
    Represents a student with a name and grade.
    """
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        """"Returns the student's grade"""
        return self._grade

    def get_name(self):
        """Returns the student's name"""
        return self._name


def student_stats(students):
    """
    Calculates the mean, medium, and mode for a list of student's grades
    :param students: list of Student objects
    :return: mean, medium, and mode in tuple
    """
    grades = []
    for student in students:
        grades.append(student.get_grade())
    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)
    return mean, median, mode