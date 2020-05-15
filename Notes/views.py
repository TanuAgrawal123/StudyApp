from django.shortcuts import render
from .models import Notes, Teacher, Student
def home(request):
    return render(request, 'Notes/home.html')

def notes(request):
	Notess=Notes.objects.all()
	return render(request, 'Notes/notesyearwise.html', {'Notes':Notess})

def notesyrbranch(request ,year, branch):
	notes_cs_details = Notes.objects.filter(branch=branch).filter(year=year)
    
	return render(request,'Notes/notescs.html/',{'notes_cs_details':notes_cs_details})

	

