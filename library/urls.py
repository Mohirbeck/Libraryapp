from django.urls import path
from .views import index, login_stu, books, user_page, logout_views, addbook, addstudent, get_book, student_page, receive_book

urlpatterns = [
    path('', index, name="index"),
    path('login_stu/', login_stu, name="student_login"),
    path('books/', books, name="books"),
    path('users/<int:pk>/', user_page, name="user_page"),
    path('logout/', logout_views, name="logout"),
    path('addbook/', addbook, name="addbook"),
    path('addstudent/', addstudent, name="addstudent"),
    path('books/<int:pk>/<int:id>', get_book, name="get_book"),
    path('students/<int:pk>/', student_page, name="student_page"),
    path('receive/<int:pk>/<int:id>', receive_book, name="receive_book"),
]
