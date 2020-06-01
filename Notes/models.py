from django.db import models

from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

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


class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	Name=models.CharField(max_length=50,null=True)
	Year=models.CharField(choices=year_choice, max_length=10)
	Branch=models.CharField( max_length=20, choices=Branch_choice, default='BTECH COMMON')
	Email=models.EmailField(null=True)
	liked=models.ManyToManyField(User, related_name='topic_liked')


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
	liked=models.ManyToManyField(User, blank=True, related_name='liked')
	disliked=models.ManyToManyField(User,blank=True, related_name='disliked')



	def __str__(self):
		return self.subject

	def num_likes(self):
		return self.liked.count()

	
	def num_dislikes(self):
		return self.disliked.count()
	
    






	

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
	liked=models.ManyToManyField(User,blank=True ,related_name='papersliked')
	disliked=models.ManyToManyField(User, blank=True, related_name='papersdisliked')


	def __str__(self):
		return self.subject
	@property
	def num_likes(self):
		return self.liked.all().count()

	def num_dislikes(self):
		return self.disliked.count()
	
    
class Pdfbooks(models.Model):
	
	subject=models.CharField(max_length=50)
	year=models.CharField(choices=year_choice,max_length=10,default='1st')
	branch=models.CharField( max_length=20, choices=Branch_choice, default='BTECH COMMON')
	author=models.CharField(max_length=50)
	published_year=models.IntegerField(null=True)
	pdf=models.FileField(upload_to="document/")
	liked=models.ManyToManyField(User,blank=True, related_name='pdfbooksliked')
	disliked=models.ManyToManyField(User, blank=True, related_name='pdfbooksdisliked')



	def __str__(self):
		return self.subject
	@property
	def num_likes(self):
		return self.liked.all().count()

	def num_dislikes(self):
		return self.disliked.count()
	
    

LIKE_CHOICES=[('upvote','upvote'),('downvote','downvote')]
class Like(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	value=models.CharField(choices=LIKE_CHOICES,default='upvote', max_length=10)
	notes=models.ForeignKey(Notes,on_delete=models.CASCADE, related_name='notes_like')
	pdf=models.ForeignKey(Pdfbooks,on_delete=models.CASCADE, related_name='pdf_like')
	paper=models.ForeignKey(Papers, on_delete=models.CASCADE, related_name='papers_like')












	
