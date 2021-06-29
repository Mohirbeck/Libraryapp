from django.contrib import admin
from .models import Librarian, Student, Book, Genre, Language

# Register your models here.
admin.site.register(Librarian)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)