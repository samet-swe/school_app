from django.shortcuts import render, get_object_or_404
from .models import User, Room, Message, Assignment, Student, Teacher, Parent, Grade

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    logins = {}
    userData = []
    allUsers = User.objects.all()
    
    for u in allUsers:
        userData = [u.password, u.role, u.id]
        logins[u.username] = userData
    
    context = {"authUsers": [logins,]}

    return render(request, "login.html", context)

def student_view(request, id):
    student = get_object_or_404(User, pk=id)
    return render(request, "student.html", {"student":student})

def teacher_view(request, id):
    teacher = get_object_or_404(User, pk=id)
    return render(request, "teacher.html", {"teacher":teacher})

def assignment_view(request):
    return render(request, "assignment.html")

def grade_view(request):
    return render(request, "grades.html")

