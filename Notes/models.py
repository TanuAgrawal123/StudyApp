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
    ('BTECH COMMON', 'BTECH COMMON'),

    
]

year_choice=[
('1st','1st'),('2nd','2nd'),('3rd','3rd'),('Final','Final'),
]

year_stu_choice=[
(1,1),(2,2),(3,3),(4,4)]
class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	Name=models.CharField(max_length=50,null=True)
	Year=models.IntegerField(default=1)
	Branch=models.CharField( max_length=20, choices=Branch_choice, default='BTECH COMMON')
	Email=models.EmailField(null=True)

	def __str__(self):
		return self.user.username

@receiver(post_save,sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
	if created:
		Student.objects.create(user=instance)
	instance.student.save()


class Teacher(models.Model):
	Name=models.CharField(max_length=50)
	Department=models.CharField( max_length=20, choices=Branch_choice)
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
	year=models.CharField(choices=year_choice ,max_length=10,default='1st')
	upvote=models.IntegerField(default=0)
	downvote=models.IntegerField(default=0)








	

class Papers(models.Model):
	subject=models.CharField(max_length=30)
	branch=models.CharField(
        max_length=10,
        choices=Branch_choice,
        default=0,)
	year=models.CharField(choices=year_choice,max_length=10,default='1st')
	data=models.FileField(upload_to="document/")
	Date_of_upload=models.DateTimeField(default=timezone.now)
	
	Type_of_paper=models.CharField(max_length=10, choices=[('EndSem','EndSem'), ('ClassTest','ClassTest')], default='EndSem')

	
class Pdfbooks(models.Model):
	
	subject=models.CharField(max_length=50)
	year=models.CharField(choices=year_choice,max_length=10,default='1st')
	branch=models.CharField( max_length=20, choices=Branch_choice, default='BTECH COMMON')
	author=models.CharField(max_length=50)
	published_year=models.IntegerField(null=True)
	pdf=models.FileField(upload_to="document/")


	






	
