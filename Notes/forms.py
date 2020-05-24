from django import forms
from .models import Notes, Pdfbooks, Papers, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
	Branch=forms.ChoiceField(choices=Branch_choice)
	Email=forms.EmailField(max_length=50)
	Year=forms.ChoiceField(choices=year_choice)

	class Meta:
		model=User
		fields=('username','Name', 'Year','Branch', 'Email','password1','password2',)

class ContributionBookForm(forms.ModelForm):
	class Meta:
		model=Pdfbooks
		fields=['year', 'branch', 'subject', 'author', 'published_year','pdf']

class ContributionPaperForm(forms.ModelForm):
	class Meta:
		model=Papers
		fields=['year', 'branch', 'subject', 'Date_of_upload','Type_of_paper','data']
