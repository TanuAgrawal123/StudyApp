from django import forms
from .models import Notes, Pdfbooks, Papers, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContributionNoteForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=['year', 'branch', 'subject', 'teacher', 'data']



class SignUpForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['Name', 'Year','Branch', 'Email']