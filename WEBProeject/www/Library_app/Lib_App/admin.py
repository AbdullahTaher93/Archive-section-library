from django.contrib import admin

from Lib_App.models import books,books_types

# Register your models here.

admin.site.register(books)
admin.site.register(books_types)