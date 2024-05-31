from django.shortcuts import render, get_object_or_404
from .models import User, Room, Message, Assignment, Student, Teacher, Parent, Grade

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
    userData = get_object_or_404(User, pk=id)
    rem_room_with_comma = userData.display_room().replace("General Announcements, ", "")
    room_list = rem_room_with_comma.replace("General Announcements", "")
    student = {"name":str(userData), "room":room_list}
    return render(request, "student.html", {"student":student})

def teacher_view(request, id):
    userData = User.objects.get(pk=id)
    rem_room_with_comma = userData.display_room().replace("General Announcements, ", "")
    room_list = rem_room_with_comma.replace("General Announcements", "")
    teacher = {"name":str(userData), "room":room_list}
    return render(request, "teacher.html", {"teacher":teacher})

def office(request, id):
    userData = get_object_or_404(User, pk=id)
    rem_room_with_comma = userData.display_room().replace("General Announcements, ", "")
    room_list = rem_room_with_comma.replace("General Announcements", "")
    office = {"name":str(userData), "room":room_list}
    return render(request, "office.html", {"office":office})

def assignment_view(request):
    return render(request, "assignment.html")

def grade_view(request):
    return render(request, "grades.html")

def contact(request):
    return render(request, "contact.html")

