from django.db import models

from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



Branch_choice = [
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('EE', 'EE'),
    ('ECE', 'ECE'),
    ('ME', 'ME'),
    ('CE', 'CE'),
    ('CH', 'CH'),
    ('NOBRANCH', 'NOBRANCH'),

    
]

year_choice=[
(1,1),(2,2),(3,3),(4,4),
]


class Student(models.Model):
	Name=models.CharField(max_length=50,null=True)
	Year=models.IntegerField(default=1)
	Branch=models.CharField(max_length=50)
	Email=models.EmailField(null=True)

	def __str__(self):
		return self.Name
	



class Teacher(models.Model):
	Name=models.CharField(max_length=50)
	Department=models.CharField(max_length=50)
	Mobile=models.BigIntegerField()
	Email=models.EmailField(null=True)
	def __str__(self):
		return self.Name


class Notes(models.Model):
	subject=models.CharField(max_length=50)
	teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
	data=models.FileField(upload_to="document/")
	Date_of_upload=models.DateTimeField(default=timezone.now)
	branch=models.CharField(
        max_length=10,
        choices=Branch_choice,
        default=0,)
	year=models.IntegerField(choices=year_choice, default=1,)
	upvote=models.IntegerField(default=0)
	downvote=models.IntegerField(default=0)
	

class Papers(models.Model):
	subject=models.CharField(max_length=30)
	branch=models.CharField(
        max_length=10,
        choices=Branch_choice,
        default=0,
    )
	data=models.FileField(upload_to="")
	Date_of_upload=models.DateTimeField(default=timezone.now)
	batch=models.IntegerField(choices=year_choice, default=1,)
	Type_of_paper=models.CharField(max_length=10, choices=[('1','EndSem'), ('2','ClassTest')], default='EndSem')

class Pdfbooks(models.Model):
	branch=models.CharField(
        max_length=10,
        choices=Branch_choice,
        default=0,)
	subject=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	published_year=models.IntegerField(null=True)
	pdf=models.FileField(upload_to="#")


	






	
