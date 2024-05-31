from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("login/", views.login, name="login"),
    path("student/<int:id>/", views.student_view, name="student"),
    path("teacher/<int:id>/", views.teacher_view, name="teacher"),
    path("office/<int:id>/", views.office, name="office"),
    path("assignment/", views.assignment_view, name="assignment"),
    path("grade/", views.grade_view, name="grade"),
    path("contact/", views.contact, name="contact")
    
]
