from django.urls import path
from . import views

application = 'regserv'

urlpatterns = [
    path('', views.index, name="index"),
    path('/data/students/', views.StudentListView.as_view(), name="api_students"),
    path('/students/', views.StudentListForm.as_view(), name="students"),
    path('/createstudent/', views.StudentCreateForm.as_view(), name="create_student")
]