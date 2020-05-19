from django import forms
from .models import Notes, Pdfbooks, Papers, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContributionNoteForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=['year', 'branch', 'subject', 'teacher', 'data']



class SignUpForm(UserCreationForm):
	Name=forms.CharField(max_length=50)
	Branch=forms.CharField()
	Email=forms.EmailField(max_length=50)
	Year=forms.IntegerField()

	class Meta:
		model=User
		fields=('username','Name', 'Year','Branch', 'Email','password1','password2',)
		