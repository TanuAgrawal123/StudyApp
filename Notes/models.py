from django.db import models

from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
	Name=models.CharField(max_length=50)
	Year=models.IntegerField()
	Branch=models.TextField(max_length=50)
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
	data=models.FileField(upload_to="")
	Date_of_upload=models.DateTimeField(default=timezone.now)
	branch=models.CharField(max_length=50, null=True)
	year=models.IntegerField(default=1)
	
	upvote=models.IntegerField(default=0)
	downvote=models.IntegerField(default=0)
	owner_of_notes=models.ForeignKey(Student, on_delete=models.CASCADE)


class Papers(models.Model):
	subject=models.CharField(max_length=30)
	branch=models.CharField(max_length=50)
	data=models.FileField(upload_to="")
	Date_of_upload=models.DateTimeField(default=timezone.now)
	batch=models.CharField(max_length=10)
	Type_of_paper=models.CharField(max_length=10, default='EndSem')

class Pdfbooks(models.Model):
	subject=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	published_year=models.IntegerField(null=True)
	pdf=models.FileField(upload_to="#")


	






	
