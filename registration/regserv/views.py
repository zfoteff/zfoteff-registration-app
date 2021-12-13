from django.http import HttpResponse
from .serializers import *
from rest_framework import generics
from django.views.generic import ListView, CreateView

def index(request):
    return HttpResponse("Hello world from django backend")

class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentListForm(ListView):
    model = Student

class StudentCreateForm(CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'schoolyear', 'major', 'gpa']
