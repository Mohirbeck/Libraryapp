from django.shortcuts import redirect, render
from .models import Book, Student, Librarian
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BookForm, StudentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'library/index.html')


def login_stu(request):
    if request.method == "POST":
        username = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "library/student_login.html", {
                "uname": username,
                "pwd": pwd
            })
    return render(request, 'library/student_login.html')


@login_required(login_url='student_login')
def books(request):
    books = Book.objects.all().order_by("-id")
    books_paginator = Paginator(books, 18)

    page_num = request.GET.get('page')

    if not request.user.is_staff:
        student = Student.objects.get(user=request.user)
    else:
        student=0

    page = books_paginator.get_page(page_num)

    return render(request, 'library/books.html', {
        "books": books,
        'books_paginator': books_paginator,
        "page": page,
        "student": student
    })


def user_page(request, pk):
    user = User.objects.get(id=pk)
    if user.is_staff:
        if request.method == "POST":
            return redirect("student_page", request.POST['select'])
        librarian = Librarian.objects.get(user=user)
        students = Student.objects.all()
        return render(request, 'library/user_page.html', {
            "user": user,
            "librarian": librarian,
            "students": students
        })

    else:
        student = Student.objects.get(user=user)
        return render(request, 'library/user_page.html', {
            "user": user,
            "student": student
        })


def logout_views(request):
    logout(request)

    return redirect("student_login")


def addbook(request):
    form = BookForm()
    if request.method == "POST":
        f = BookForm(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect("books")
    return render(request, "library/addbook.html", {
        "form": form
    })


def addstudent(request):
    form = StudentForm()
    if request.method == "POST":
        f = StudentForm(request.POST)
        if f.is_valid():
            user = User(username=f.cleaned_data['username'],
                        first_name=f.cleaned_data['first_name'],
                        last_name=f.cleaned_data['last_name'],
                        password=f.cleaned_data['pwd1'])
            user.save()
            student = Student(user=user, group=f.cleaned_data['group'],
                              faculty=f.cleaned_data['faculty'])
            student.save()
            return redirect("books")
        else:
            return render(request, "library/addstudent.html", {
                "form": f
            })
    return render(request, "library/addstudent.html", {
        "form": form
    })


def get_book(request, pk, id):
    book = Book.objects.get(id=pk)
    user = User.objects.get(id=id)
    student = Student.objects.get(user=user)
    student.books.add(book)
    student.save()
    book.available_copies = int(book.available_copies) - 1
    book.save()
    return redirect('user_page', request.user.id)


def student_page(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'library/student_page.html', {
        "student": student
    })


def receive_book(request, pk, id):
    book = Book.objects.get(id=pk)
    student = Student.objects.get(id=id)
    student.books.remove(book)
    student.save()
    book.available_copies = int(book.available_copies) + 1
    book.save()
    return redirect('student_page', student.id)
