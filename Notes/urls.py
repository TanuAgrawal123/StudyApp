from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('notes/<int:year>/<str:branch>',views.notesyrbranch, name='notesyrbranch'),
    
]