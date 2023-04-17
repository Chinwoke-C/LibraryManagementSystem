from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser


class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(default='', blank=True, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='1977-01-01')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    GENRE_CHOICES = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('POWER', 'POW'),
        ('COMEDY', 'COM'),
    ]
    LANGUAGE_CHOICES = [
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU'),
        ('ENGLISH', 'ENG'),
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=13, choices=GENRE_CHOICES, default='FIN')
    language = models.CharField(max_length=15, choices=LANGUAGE_CHOICES, default='YOR')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']


# class Genre(models.Model):
#     GENRE_CHOICES = [
#         ('ROMANCE', 'ROM'),
#         ('THRILLER', 'THR'),
#         ('FICTION', 'FIC'),
#         ('DRAMA', 'DRA')
#     ]
#     name = models.CharField(max_length=10, choices=GENRE_CHOICES, default='DRA')
#
#     # name = models.CharField(max_length=55)
#
#     def __str__(self):
#         return self.name


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('YORUBA', 'YOR'),
        ('ENGLISH', 'ENG'),
        ('HAUSA', 'HAU')
    ]
    name = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='ENG')

    def __str__(self):
        return self.name





class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    uniqueId = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=55, blank=False, null=False)
    borrower = models.OneToOneField(LibraryUser, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.imprint
