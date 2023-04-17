from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Book, Author, BookInstance, LibraryUser


# Register your models here.
# @admin.register(LibraryUser)
# class User(UserAdmin):
#     pass
#
#
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'genre', 'language', 'price']
    list_editable = ['price']
    list_per_page = 10
    list_filter = ['title']


# admin.site.register(Author)
# admin.site.register(BookInstance)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['due_back', 'status', 'book', 'imprint', 'borrower']
