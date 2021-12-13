from django.db import models
from django.core import validators
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse, reverse_lazy

class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    idnumber = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)

    class Meta:         
        abstract = True

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return f"PID: {self.id}: Name: {self.full_name}, SID: {self.idnumber} Email: {self.email} Created: {self.datecreated} Modified: {self.datemodified}"

class Student(Person):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    MAJORS = [
        ('CPSC', 'Computer Science'),
        ('ENGR', 'Engineering'),
        ('BUSI', 'Business'),
        ('SCIE', 'Science'),
        ('PLAW', 'Pre-Law'),
        ('NURS', 'Nursing'),
        ('UNDC', 'Undecided'),
    ]

    schoolyear = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL)
    major = models.CharField(max_length=4, choices=MAJORS)
    gpa = models.FloatField()

    def __str__(self):
        return f'Student ID: {self.id}: {super(Student, self).__str__()} - year in school {self.schoolyear}, major: {self.major}, gpa: {self.gpa}'

    def get_absolute_url(self):
        return reverse_lazy('regserve:students')