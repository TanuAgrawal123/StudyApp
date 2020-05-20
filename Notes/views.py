from django.shortcuts import render, redirect
from .models import Notes, Teacher ,Student, Pdfbooks, Papers
from .forms import ContributionNoteForm, SignUpForm, ContributionBookForm, ContributionPaperForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import  AuthenticationForm


    
def home(request, ):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)

				
				return redirect('home')

			
	form = AuthenticationForm()
	return render(request,"Notes/home.html",{"form":form})

def notes(request):
	
	return render(request, 'Notes/notesyearwise.html')

def notesyrbranch(request ,year, branch):
	notes_cs_details = Notes.objects.filter(branch=branch).filter(year=year).order_by('subject')
	return render(request,'Notes/notes.html/',{'notes_cs_details':notes_cs_details,'year':year,'branch':branch})

	
def books(request):
	return render(request,'Notes/bookyearwise.html')

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

def signup(request):
	form = SignUpForm(request.POST)
	if form.is_valid():

		user = form.save()
		user.refresh_from_db()
		user.student.Name = form.cleaned_data.get('Name')
		user.student.Year = form.cleaned_data.get('Year')
		user.student.Email = form.cleaned_data.get('Email')
		user.student.Branch=form.cleaned_data.get('Branch')
		user.save()
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password1')
		user = authenticate(username=username, password=password)
		login(request,user)
		return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'Notes/signup.html', {'form': form})

def logout_account(request):
	logout(request)
	return redirect('home')


def booksyrbranch(request, year, branch):
	books_cs_details = Pdfbooks.objects.filter(branch=branch).filter(year=year).order_by('subject')
	return render(request,'Notes/books.html/',{'books_cs_details':books_cs_details,'year':year,'branch':branch})


def Books_form(request):
	if request.method == "POST":
		
		form = ContributionBookForm(request.POST, request.FILES)
		if form.is_valid():
			books= form.save(commit=False)
			books.save()
	
			
			return redirect('home')
	else:
		form = ContributionBookForm()
		return render(request, 'Notes/contributionbookform.html', {'form': form})

def Papers_form(request):
	if request.method == "POST":
		
		form = ContributionPaperForm(request.POST, request.FILES)
		if form.is_valid():
			papers= form.save(commit=False)
			papers.save()
	
			
			return redirect('home')
	else:
		form = ContributionPaperForm()
		return render(request, 'Notes/contributionpaperform.html', {'form': form})

def papers(request):
	
	return render(request, 'Notes/paperyearwise.html')

def papersyrbranch(request, year, branch):
	papers_cs_details = Papers.objects.filter(branch=branch).filter(year=year).order_by('Type_of_upload').order_by('subject')
	return render(request,'Notes/papers.html/',{'papers_cs_details':papers_cs_details,'year':year,'branch':branch})

