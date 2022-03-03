from django.contrib import admin

# Register your models here. or Register newly added tables.

from .models import Book

admin.site.register(Book)
