from django.shortcuts import render, redirect
from .models import Notes, Teacher, Student
from .forms import ContributionNoteForm
from django.core.files.storage import FileSystemStorage

    
def home(request):
	return render(request, 'Notes/home.html')

def notes(request):
	
	return render(request, 'Notes/notesyearwise.html')

def notesyrbranch(request ,year, branch):
	notes_cs_details = Notes.objects.filter(branch=branch).filter(year=year)
	
	return render(request,'Notes/notes.html/',{'notes_cs_details':notes_cs_details})

	
def books(request):
	return render(request, 'Notes/book.html')

def Notes_form(request):
	if request.method == "POST":
		
		form = ContributionNoteForm(request.POST, request.FILES)
		if form.is_valid():
			notes = form.save(commit=False)
			notes.save()
			
			
			return redirect('home')

	else:
		form = ContributionNoteForm()
	return render(request, 'Notes/contributionform.html', {'form': form})
