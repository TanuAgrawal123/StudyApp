from django import forms
from .models import Notes, Pdfbooks, Papers

class ContributionNoteForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=['year', 'branch', 'subject', 'teacher', 'data']





