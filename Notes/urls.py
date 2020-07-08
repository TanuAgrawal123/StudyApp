from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('notes/<str:year>/<str:branch>',views.notesyrbranch, name='notesyrbranch'),
    path('books/', views.books, name='books'),
    path('bokes/<str:year>/<str:branch>', views.booksyrbranch, name='booksyrbranch'),
    path('Notesform/', views.Notes_form, name='Notes_form'),
    path('signupstudent/',views.StudentSignupView.as_view(), name='signup'),
    path('logout/', views.logout_account, name='logout'),
    path('Booksform/', views.Books_form, name='Books_form'),
    path('Papersform/', views.Papers_form, name='Papers_form'),
    path('papers/',views.papers, name='papers'),
    path('papers/<str:year>/<str:branch>', views.papersyrbranch, name='papersyrbranch'),
    path('faculty_list/<str:branch>', views.facultylist, name='facultylist'),
    path('announcement', views.announcement, name='announcement'),
    path('notes/<str:year>/<str:branch>/likes/',views.likes_notes, name='likes_notes'),
    path('notes/<str:year>/<str:branch>/dislikes/', views.dislikes_notes,name='dislikes_notes'),
    path('papers/<str:year>/<str:branch>/dislikes/', views.dislikes_papers,name='dislikes_papers'),
    path('papers/<str:year>/<str:branch>/likes/',views.likes_papers, name='likes_papers'),
    path('books/<str:year>/<str:branch>/dislikes/', views.dislikes_books,name='dislikes_books'),
    path('books/<str:year>/<str:branch>/likes/',views.likes_books, name='likes_books'),
     path('signupfaculty/',views.TeacherSignupView.as_view(), name='signupteacher'),
    path('disccussionpanel', views.post_list, name='discussion_list'),
path('disccusion/<int:pk>/', views.post_detail, name='disccusion_detail'),
#path('disccusion/new', views.disccusion_new, name='disccusion_new'),

#path('disccusion/<int:pk>/edit/', views.disccusion_edit, name='disccusion_edit'),
path('disccusion/<int:pk>/answer/', views.post_detail, name='add_answer_to_disccusion'),
path('answer/<int:pk>/likes',views.likes_answer, name='likes_answer'),
    path('answer/<int:pk>/dislikes/', views.dislikes_answer,name='dislikes_answer'),
    path('disccusion/ask_doubt', views.post_new, name='ask_doubt'),





    
]