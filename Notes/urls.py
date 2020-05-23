from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('notes/<str:year>/<str:branch>',views.notesyrbranch, name='notesyrbranch'),
    path('books/', views.books, name='books'),
    path('bokes/<str:year>/<str:branch>', views.booksyrbranch, name='booksyearwise'),
    path('Notesform/', views.Notes_form, name='Notes_form'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout_account, name='logout'),
    path('Booksform/', views.Books_form, name='Books_form'),
    path('Papersform/', views.Papers_form, name='Papers_form'),
    path('papers/',views.papers, name='papers'),
    path('papers/<str:year>/<str:branch>', views.papersyrbranch, name='papersyrbranch'),
    path('faculty_list/<str:branch>', views.facultylist, name='facultylist'),
    path('announcement', views.announcement, name='announcement'),




    
]