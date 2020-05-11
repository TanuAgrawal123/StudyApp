from rest_framework import serializers
from .models import Notes, Papers, Student, Teacher, pdfBooks

class NotesSerializers(serializers.ModelSerializer):
	class Meta:
		model=Notes
		fields=['subject', 'teacher', 'data', 'batch']


class PaperSerializers(serializers.ModelSerializer):
	class Meta:
		model=Notes
		fields=['subject', 'data', 'Type_of_paper']


class BookSerializers(serializers.ModelSerializer):
	class Meta:
		model=Notes
		fields=['subject', 'author', 'pdf']


