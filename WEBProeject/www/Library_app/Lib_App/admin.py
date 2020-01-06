from django.contrib import admin

from Lib_App.models import books,books_types,persons,borrowerbook,returnbook

# Register your models here.

admin.site.register(books)
admin.site.register(books_types)
admin.site.register(persons)
admin.site.register(borrowerbook)
admin.site.register(returnbook)