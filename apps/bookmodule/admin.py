from django.contrib import admin
from .models import Book, Address, Student, Publisher, Author, Book2

admin.site.register(Address)
admin.site.register(Student)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book2)
# Register your models here.
