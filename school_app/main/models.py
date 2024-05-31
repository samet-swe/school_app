from django.db import models
from django.contrib.postgres.fields import ArrayField
from sqlalchemy import ForeignKey

class Room(models.Model):
    name = models.CharField(max_length = 30, unique = True, blank = False)
    #members = models.ManyToManyField(User, through = "Membership", through_fields = ("room", "person"), related_name = "rooms")
    #msgs = models.ManyToManyField(Messages, on_delete = models.CASCADE, related_name = "rooms_posted_to")
    #parents = models.ManyToManyField(Parents, through = "Membership", through_fields = ("room", "parent"), related_name = "room")
    #teacher = models.ForeignKey(Teachers, related_name = "room")
    
    def display_members(self):
        ''' Create a string for all the members of a requested room. '''
        return ', '.join(str(members) for members in self.members.all()) 
           
    def __str__(self):
        ''' Overwrite the str() function to return the requested room's name. '''
        return self.name
    
class User(models.Model):
    username = models.CharField(max_length=20, unique = True, blank = False)
    password = models.CharField(max_length=20, blank = False)
    first_name = models.CharField(max_length = 20, blank = False)
    last_name = models.CharField(max_length = 20, blank = False)
    room = models.ManyToManyField(Room, related_name = "members", blank = False)
    #room = models.ManyToManyField(Room, through = "Membership", through_fields = ("room", "person"), related_name = "members")
    #rooms = ArrayField(models.CharField(max_length = 30), null = True)
    
    class Role(models.TextChoices):
        Teacher = "Te"
        Office = "Of"
        Parent = "Pa"
        Student = "St"
        
    role = models.CharField(max_length=2, choices = Role, default = Role.Student)
        
    #personal_msgs = models.ManyToManyField(Messages, on_delete = models.CASCADE, related_name = "person_posted_to")
    
    def display_room(self):
        ''' Create a string for all the rooms to which a requested user has access. '''
        return ', '.join(room.name for room in self.room.all())
    
    def __str__(self):
        ''' Overwrite the str() function to return the requested user's full name. '''
        return f"{self.first_name} {self.last_name}"

#class Membership(models.Model):
#    room = models.ForeignKey(Room, on_delete = models.CASCADE)
#    person = models.ForeignKey(User, on_delete = models.CASCADE)
    
class Message(models.Model):
    msg = models.TextField(max_length = 200, blank = False)
    when_posted = models.DateTimeField(blank = False)
    who_posted = models.CharField(max_length = 41, blank = False)
    person_posted_to = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name = "personal_msgs")
    room_posted_to = models.ForeignKey(Room, on_delete = models.DO_NOTHING, related_name = "msgs")
    
class Assignment(models.Model):
    name = models.CharField(max_length = 50, blank = False)
    due_date = models.DateField(blank = False)
    out_of_how_many = models.IntegerField(blank = False, default = 100)
    take_home = models.BooleanField(blank = False, default = True)
    extra_credit = models.BooleanField(blank = False, default = False)
    assigned_to = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = "assignments")
        
class Student(models.Model):
    student = models.OneToOneField(User, on_delete = models.CASCADE)
    
class Teacher(models.Model):
    teacher = models.OneToOneField(User, on_delete = models.CASCADE)
    
class Parent(models.Model):
    parent = models.OneToOneField(User, on_delete = models.CASCADE)
    childUsername = models.CharField(max_length = 20, default = "student")
    relationship = models.CharField(max_length = 30, default = "parent")
    
class Grade(models.Model):
    points = models.DecimalField(max_digits = 4, decimal_places = 1)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "grades") 
    
    