from django.shortcuts import render

def home(request):
    return render(request, 'Notes/home.html')

def notes(request):
	return render(request, 'Notes/notesyearwise.html')
	

