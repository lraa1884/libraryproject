from django.contrib import admin
from .models import Book, Address, Student

admin.site.register(Address)
admin.site.register(Student)
# Register your models here.
