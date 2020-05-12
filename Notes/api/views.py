from ..models import Notes, Papers, Teacher, Pdfbooks
from .serializers import BooksSerializers, NotesSerializers, TeacherSerializers, PapersSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
	def get(sel, request, format=None):
		book=Pdfbooks.objects.all()
		serializer = BookSerializers(book, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = BookSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotesList(APIView):
	def get(sel, request, format=None):
		notes=Notes.objects.all()
		serializer = NotesSerializers(notes, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = NotesSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PapersList(APIView):
	def get(sel, request, format=None):
		papers=Papers.objects.all()
		serializer = PapersSerializers(papers, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = PapersSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherList(APIView):
	def get(self, request, format=None):
		staff=Teacher.objects.all()
		serializer = TeacherSerializers(staff, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = TeacherSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)