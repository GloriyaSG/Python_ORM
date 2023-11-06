import os
import django
from datetime import datetime

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Student

# Create and check models

def add_students():
    students = [('FC5204', 'John', 'Doe', '15/05/1995', 'john.doe@university.com'),
                ('FE0054', 'Jane',	'Smith', 'NULL', 'jane.smith@university.com'),
                ('FH2014', 'Alice', 'Johnson', '10/02/1998', 'alice.johnson@university.com'),
                ('FH2015',	'Bob',	'Wilson', '25/11/1996',	'bob.wilson@university.com'),]
    for st in students:
        st_id, st_name, st_last_name, st_date, st_mail = st

        if st_date == 'NULL':
            student = Student.objects.create(
                student_id=st_id,
                first_name=st_name,
                last_name=st_last_name,
                email=st_mail,
            )
        else:
            student = Student.objects.create(
                student_id=st_id,
                first_name=st_name,
                last_name=st_last_name,
                birth_date=datetime.strptime(st_date, "%d/%m/%Y").strftime("%Y-%m-%d"),
                email=st_mail
            )
        student.save()

# Run and print your queries
print(Student.objects.all())
