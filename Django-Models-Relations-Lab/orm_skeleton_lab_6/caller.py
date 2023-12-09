import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Lecturer, Subject, Student
# Create and check models
# Run and print your queries


# # keep the data from the previous exercise, so you can reuse it
#
# lecturer1 = Lecturer.objects.create(first_name="John", last_name="Doe")
# lecturer2 = Lecturer.objects.create(first_name="Jane", last_name="Smith")
# Subject.objects.create(name="Mathematics", code="MATH101", lecturer=lecturer1)
# Subject.objects.create(name="History", code="HIST101", lecturer=lecturer2)
# Subject.objects.create(name="Physics", code="PHYS101", lecturer=lecturer1)
# math_subject = Subject.objects.get(name="Mathematics")
# math_lecturer = math_subject.lecturer
# print(f"The lecturer for Mathematics is {math_lecturer}.")
#
# history_subject = Subject.objects.get(name="History")
# history_lecturer = history_subject.lecturer
# print(f"The lecturer for History is {history_lecturer}.")
#
# physics_subject = Subject.objects.get(name="Physics")
# physics_lecturer = physics_subject.lecturer
# print(f"The lecturer for Physics is {physics_lecturer}.")
#
# student1 = Student.objects.create(student_id="M1051", first_name="Alice", last_name="Johnson", birth_date="2000-01-15", email="a.johnson@abv.bg")
# student2 = Student.objects.create(student_id="S217", first_name="Bob", last_name="Smith", birth_date="2001-05-20", email="bobby@gmail.com")
# subject1 = Subject.objects.get(name="Mathematics")
# subject2 = Subject.objects.get(name="History")
# subject3 = Subject.objects.get(name="Physics")
# student1.subjects.add(subject1, subject2)
# student2.subjects.add(subject1, subject2, subject3)
#
# math_subject = Subject.objects.get(name="Mathematics")
# math_students = math_subject.student_set.all()
# for student in math_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in Mathematics.")
#
# history_subject = Subject.objects.get(name="History")
# history_students = history_subject.student_set.all()
# for student in history_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in History.")
#
# physics_subject = Subject.objects.get(name="Physics")
# physics_students = physics_subject.student_set.all()
# for student in physics_students:
#     print(f"{student.first_name} {student.last_name} is enrolled in Physics.")
#
from django.test import TestCase
from main_app.models import Lecturer, Subject, Student

class ModelRelationshipTest(TestCase):
    def setUp(self):
        # Create lecturers
        self.lecturer1 = Lecturer.objects.create(first_name="John", last_name="Doe")
        self.lecturer2 = Lecturer.objects.create(first_name="Jane", last_name="Smith")

        # Create subjects and associate with lecturers
        self.mathematics = Subject.objects.create(name="Mathematics", code="MATH101", lecturer=self.lecturer1)
        self.history = Subject.objects.create(name="History", code="HIST101", lecturer=self.lecturer2)
        self.physics = Subject.objects.create(name="Physics", code="PHYS101", lecturer=self.lecturer1)

        # Create students
        self.student1 = Student.objects.create(
            student_id="M1051",
            first_name="Alice",
            last_name="Johnson",
            birth_date="2000-01-15",
            email="a.johnson@abv.bg"
        )
        self.student2 = Student.objects.create(
            student_id="S217",
            first_name="Bob",
            last_name="Smith",
            birth_date="2001-05-20",
            email="bobby@gmail.com"
        )

        # Associate students with subjects
        self.student1.subjects.add(self.mathematics, self.history)
        self.student2.subjects.add(self.mathematics, self.history, self.physics)

    def test_subject_students(self):
        math_subject = Subject.objects.get(name="Mathematics")
        math_students = math_subject.student_set.all()

        # Check if the students are associated with the Mathematics subject
        self.assertEqual(len(math_students), 2)
        self.assertIn(self.student1, math_students)
        self.assertIn(self.student2, math_students)

        history_subject = Subject.objects.get(name="History")
        history_students = history_subject.student_set.all()

        # Check if the students are associated with the History subject
        self.assertEqual(len(history_students), 2)
        self.assertIn(self.student1, history_students)
        self.assertIn(self.student2, history_students)

        physics_subject = Subject.objects.get(name="Physics")
        physics_students = physics_subject.student_set.all()

        # Check if the students are associated with the Physics subject
        self.assertEqual(len(physics_students), 1)
        self.assertIn(self.student2, physics_students)