from django import forms
from .models import Notes, Pdfbooks, Papers, Student ,Teacher, User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



class ContributionNoteForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=['year', 'branch', 'subject', 'teacher', 'data']

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


class SignUpForm(UserCreationForm):
	Name=forms.CharField(max_length=50)
	Email=forms.EmailField()
	Year=forms.ChoiceField(choices=year_choice, )
	Branch=forms.ChoiceField(choices=Branch_choice)


	
	class Meta(UserCreationForm.Meta):
		model=	User


	@transaction.atomic
	def save(self):
		user = super().save(commit=False)
		user.is_student = True
		user.save()
		student = Student.objects.create(user=user)
		student.Year=self.cleaned_data.get('Year')
		student.Branch=self.cleaned_data.get('Branch')
		student.Name=self.cleaned_data.get('Name')
		student.Email=self.cleaned_data.get('Email')
		student.save()
		return user
		
class SignUpFormFaculty(UserCreationForm):
	Name=forms.CharField(max_length=50)
	Email=forms.EmailField()
	Mobile=forms.CharField(required=True)
	Department=forms.ChoiceField(choices=Branch_choice)

	
	class Meta(UserCreationForm.Meta):
		model=	User


	@transaction.atomic
	def save(self):
		print("start")
		user = super().save(commit=False)
		
		user.is_teacher = True
		user.save()
		print("sufff")
		teacher = Teacher.objects.create(user=user)
		print("done")
		teacher.Mobile=self.cleaned_data.get('Mobile')
		teacher.Department=self.cleaned_data.get('Department')
		teacher.Email=self.cleaned_data.get('Email')
		teacher.Name=self.cleaned_data.get('Name')

		
		teacher.save()
		return user


class ContributionBookForm(forms.ModelForm):
	class Meta:
		model=Pdfbooks
		fields=['year', 'branch', 'subject', 'author', 'published_year','pdf']

class ContributionPaperForm(forms.ModelForm):
	class Meta:
		model=Papers
		fields=['year', 'branch', 'subject', 'Date_of_upload','Type_of_paper','data']
