from django.shortcuts import render, redirect
from .models import Notes, Teacher ,Student, Pdfbooks, Papers, User, Answer, Post
from .forms import ContributionNoteForm, SignUpForm, ContributionBookForm,SignUpFormFaculty,AnswerForm, ContributionPaperForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.views.generic import CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

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


def likes_notes(request, year, branch):
	
	notes=get_object_or_404(Notes, id=request.POST.get('notes_id'))
	

	if request.user in notes.disliked.all():
		print("H")


		notes.disliked.remove(request.user)
		notes.liked.add(request.user)
	else:
		notes.liked.add(request.user)
	
	return redirect('notesyrbranch' ,year, branch)

def dislikes_notes(request, year, branch):
	
	notes=get_object_or_404(Notes, id=request.POST.get('notes_id'))
	

	if request.user in notes.liked.all():
		


		notes.liked.remove(request.user)
		notes.disliked.add(request.user)
	else:
		notes.disliked.add(request.user)
	
	return redirect('notesyrbranch' ,year, branch)
		
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

class StudentSignupView(CreateView):
	model=User
	form_class=SignUpForm
	template_name='Notes/signup.html'

	
	def form_valid(self,form):
		user=form.save()
		login(self.request,user)
		return redirect('home')





class TeacherSignupView(CreateView):
	model=User
	form_class=SignUpFormFaculty
	template_name='Notes/signupteacher.html'

	
	def form_valid(self,form):
		user=form.save()
		login(self.request,user)
		return redirect('home')



def logout_account(request):
	logout(request)
	return redirect('home')


def booksyrbranch(request, year, branch):
	books_cs_details = Pdfbooks.objects.filter(branch=branch).filter(year=year).order_by('subject')
	return render(request,'Notes/books.html/',{'books_cs_details':books_cs_details,'year':year,'branch':branch})

def likes_books(request, year, branch):
	
	books=get_object_or_404(Pdfbooks, id=request.POST.get('books_id'))
	

	if request.user in books.disliked.all():
		

		books.disliked.remove(request.user)
		books.liked.add(request.user)
	else:
		books.liked.add(request.user)
	
	return redirect('booksyrbranch' ,year, branch)

def dislikes_books(request, year, branch):
	
	books=get_object_or_404(Pdfbooks, id=request.POST.get('books_id'))
	

	if request.user in books.liked.all():
		

		books.liked.remove(request.user)
		books.disliked.add(request.user)
	else:
		books.disliked.add(request.user)
	
	return redirect('booksyrbranch' ,year, branch)
		

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

def facultylist(request, branch):
	facultydetails = Teacher.objects.filter(Department=branch)
	return render(request,'Notes/faculty_list.html/',{'facultydetails':facultydetails,'branch':branch})

def likes_papers(request, year, branch):
	
	papers=get_object_or_404(Papers, id=request.POST.get('papers_id'))
	

	if request.user in papers.disliked.all():
		

		papers.disliked.remove(request.user)
		papers.liked.add(request.user)
	else:
		papers.liked.add(request.user)
	
	return redirect('papersyrbranch' ,year, branch)

def dislikes_papers(request, year, branch):
	
	papers=get_object_or_404(Papers, id=request.POST.get('papers_id'))
	

	if request.user in papers.liked.all():
		

		papers.liked.remove(request.user)
		papers.disliked.add(request.user)
	else:
		papers.disliked.add(request.user)
	
	return redirect('papersyrbranch' ,year, branch)
		
def announcement(request):
	return render(request, 'Notes/announcements.html')


def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
   
    paginator = Paginator(posts_list,3,allow_empty_first_page=False)
    page=request.GET.get('page',1)
    posts=paginator.page(page)

    return render(request, 'Notes/discussion_list.html', {'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.user=request.user
                answer.created_date=timezone.now()
                answer.post = post
                answer.save()
                
    else:
        form = AnswerForm()


    return render(request, 'Notes/discussion_detail.html', {'post':post,'form': form,})

    

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('discussion_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Notes/discussion_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Notes/discussion_edit.html', {'form': form})

def add_answer_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            print(request.user)
            print("Hello")
            answer.user=request.user
            answer.created_date=timezone.now()
            answer.post = post

            answer.save()
            return redirect('discussion_detail', pk=post.pk)
    else:
        form = AnswerForm()
    return render(request, 'Notes/discussion_detail', {'form': form})


def likes_answer(request, pk):
	
	answer=get_object_or_404(Answer, id=request.POST.get('answer_id'))
	

	if request.user in answer.disliked.all():
		

		answer.disliked.remove(request.user)
		answer.liked.add(request.user)
	else:
		answer.liked.add(request.user)
	
	return redirect('disccusion_detail' ,pk)


def dislikes_answer(request, pk):
	
	answer=get_object_or_404(Answer, id=request.POST.get('answer_id'))
	

	if request.user in answer.liked.all():
		

		answer.liked.remove(request.user)
		answer.disliked.add(request.user)
	else:
		answer.disliked.add(request.user)
	
	return redirect('disccusion_detail' ,pk)