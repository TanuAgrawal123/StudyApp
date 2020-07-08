from django.db import models

from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager




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
choice=[('student','student'),('teacher','teacher')]

class User(AbstractUser):
	
	is_student=models.BooleanField(default=False)
	is_teacher=models.BooleanField(default=False)
	


class Student(models.Model):
	Name=models.CharField(max_length=50)
	Email=models.EmailField(null=True)
	
	
	user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_student',primary_key=True)
	Year=models.CharField(choices=year_choice, max_length=10)
	Branch=models.CharField( max_length=20, choices=Branch_choice, default='BTECH COMMON')
	
	liked=models.ManyToManyField(User, related_name='topic_liked')

	def __str__(self):
		return self.user.username



	

class Teacher(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
	Name=models.CharField(max_length=50, null=True)
	Email=models.EmailField(null=True)
	Department=models.CharField( max_length=20, choices=Branch_choice)
	Mobile=models.CharField(max_length=20)

	def __str__(self):
		return self.user.username
	


	


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

class Post(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=50)
	description=models.TextField()
	image=models.ImageField(upload_to='images/', null=True,blank=True)
	published_date=models.DateTimeField(default=timezone.now)
	tags = TaggableManager()
	#image=models.ImageField(upload_to='images/', default='static/Notes/images/no.png')

	

	def __str__(self):
		return self.title


class Answer(models.Model):
	post=models.ForeignKey(Post,related_name='answers',on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	
	text=models.TextField(max_length=500)
	created_date = models.DateTimeField(default=timezone.now)
	approved_answers=models.BooleanField(default=False)
	liked=models.ManyToManyField(User,blank=True ,related_name='answerliked')
	disliked=models.ManyToManyField(User, blank=True, related_name='answerdisliked')

	@property
	def num_likes(self):
		return self.liked.all().count()

	def num_dislikes(self):
		return self.disliked.count()




	def count(self):
		return self.text.all().count()


	def approve(self):
		self.approved_answers=True
		self.save()

	def __str__(self):	

		return self.text

	
    

LIKE_CHOICES=[('upvote','upvote'),('downvote','downvote')]
class Like(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	value=models.CharField(choices=LIKE_CHOICES,default='upvote', max_length=10)
	notes=models.ForeignKey(Notes,on_delete=models.CASCADE, related_name='notes_like')
	pdf=models.ForeignKey(Pdfbooks,on_delete=models.CASCADE, related_name='pdf_like')
	paper=models.ForeignKey(Papers, on_delete=models.CASCADE, related_name='papers_like')
	answer=models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_like' ,null=True)







	










