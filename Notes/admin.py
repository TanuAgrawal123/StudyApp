from django.contrib import admin

# Register your models here.
from .models import Notes, Papers, Teacher, Student

admin.site.register(Notes)
admin.site.register(Papers)
admin.site.register(Teacher)
admin.site.register(Student)
