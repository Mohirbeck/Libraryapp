from django.db import models
from django.contrib.auth.models import User


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name}, {self.employee_id}"


class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    total_copies = models.PositiveIntegerField()
    available_copies = models.IntegerField()
    pic = models.ImageField(blank=True, null=True, upload_to='book_image/')

    def __str__(self):
        return f"{self.title}, {self.author}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.user.first_name}, {self.group}"
