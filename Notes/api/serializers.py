from rest_framework import serializers
from ..models import Notes, Papers, Pdfbooks, Teacher

class NotesSerializers(serializers.ModelSerializer):
	class Meta:
		model=Notes
		fields=['subject', 'teacher','year' ,'data','Date_of_upload',]



class PapersSerializers(serializers.ModelSerializer):
	class Meta:
		model=Papers
		fields=['subject','branch', 'Date_of_upload' ,'data', 'batch','Type_of_paper']


class BooksSerializers(serializers.ModelSerializer):
	class Meta:
		model=Pdfbooks
		fields=['subject', 'author','published_year', 'pdf']

class TeacherSerializers(serializers.ModelSerializer):
	class Meta:
		model=Teacher
		fields=['Name', 'Department', 'Mobile', 'Email']


