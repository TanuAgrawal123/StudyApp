from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('notes/<int:year>/<str:branch>',views.notesyrbranch, name='notesyrbranch'),
    path('books/', views.books, name='books'),
    path('Notesform/', views.Notes_form, name='Notes_form'),
    path('signup/',views.signup, name='signup'),
    path('logout/', views.logout_account, name='logout'),

    
]