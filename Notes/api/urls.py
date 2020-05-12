from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Notes.api import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('notes/', views.NotesList.as_view()),
    path('papers/', views.PapersList.as_view()),
    path('teachers/', views.TeacherList.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)