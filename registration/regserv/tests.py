from django.test import TestCase, Client
from .serializers import StudentSerializer
from .models import *
import logging
import io
from rest_framework.parsers import JSONParser

# http://localhost:8000/regserve/data/students/

logger = logging.getLogger()

class DataTest(TestCase):
    def setUp(self):
        student1 = Student.objects.create(
            firstname="First", 
            lastname="Student",
            idnumber=100,
            email="first@student.edu",
            schoolyear="SR",
            major="CS",
            gpa=4.0,)

        student2 = Student.objects.create(
            firstname="Second", 
            lastname="Student",
            idnumber=101,
            email="second@student.edu",
            schoolyear="SR",
            major="ENG",
            gpa=2.0,)
        self.test_client = Client()

    def test_student_api(self):
        students_response = self.test_client.get('/regserve/data/students/')
        logger.log(f'\nTEST_STUDENT_API| api response {students_response} Status: {students_response.status_code}')
        self.assertEqual(students_response.status_code, 200)
        logger.log(f'\nTEST_STUDENT_API| api response content: {students_response.content}')
        student_stream = io.BytesIO(students_response.content)
        logger.log(f'\nTEST_STUDENT_API| api response stream: {student_stream}')
        student_data = JSONParser().parse(student_stream)
        first_student_data = student_data[0]
        logger.log(f'\nTEST_STUDENT_API| api response data: {first_student_data} ID: {first_student_data["id"]}')
        first_student_db = Student.objects.get(id=first_student_data['id'])
        logger.log(f'\nTEST_STUDENT_API| student object from DB is: {first_student_db}')

        first_student_serializer = StudentSerializer(first_student_db , data=first_student_data)
        logger.log(f'\nTEST_STUDENT_API| response serializer: {first_student_serializer}')
        logger.log(f'\nTEST_STUDENT_API| response validity: {first_student_serializer.is_valid()}')
        logger.log(f'\nTEST_STUDENT_API| response data: {first_student_serializer.validated_data}')
        first_student_api = first_student_serializer.save()
        logger.log(f'\nTEST_STUDENT_API| api response object is : {first_student_api}')
        self.assertEqual(first_student_db, first_student_api)

    def test_student1(self): 
        student_list = Student.objects.all()
        student = student_list[0]
        logger.log(f'\nTEST_STUDENT| Student: {student}')
        self.assertEqual(student.id, 1)
        self.assertEqual(student.full_name, 'First Student')
        self.assertEqual(student.idnumber, 100)

    def test_student1(self): 
        student_list = Student.objects.all()
        student = student_list[1]
        logger.log(f'\nTEST_STUDENT| Student: {student}')
        self.assertEqual(student.id, 2)
        self.assertEqual(student.full_name, 'Second Student')
        self.assertEqual(student.idnumber, 101)

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_response(self):
        response = self.test_client.get('/regserv')
        logger.log(f'\nSimple response test: {response}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello from django backend")
