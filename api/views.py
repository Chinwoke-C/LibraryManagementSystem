from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

import book
from api import serializers
from api.pagination import DefaultPageNumberPagination
from api.permissions import IsAdminOrReadOnly
from api.serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, BookInstanceSerializer
from book.models import Book, Author, BookInstance


# Create your views here.
# def book_list(request):
#     queryset = Book.objects.all()
#     serializer = BookSerializer(book)
#     return serializers.data


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         book = BookCreatSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("book saved successfully")
#
#
# # class BookListView(generics.ListAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# @api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# def book_details(request, pk):
#     # try:
#     #     book = Book.objects.get(pk=pk)
#     #
#     # except Book.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # if request.method == 'DELETE':
#     #     book.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def author_details(request):
#     if request.method == 'GET':
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def author_name(request, pk):
#     if request.method == 'GET':
#         queryset = Author.objects.get(pk=pk)
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)
class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class AuthorCreateApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # class SnippetDetail(APIView):
    #     """
    #     Retrieve, update or delete a snippet instance.
    #     """
    #
    #     def get_object(self, pk):
    #         try:
    #             return Snippet.objects.get(pk=pk)
    #         except Snippet.DoesNotExist:
    #             raise Http404
    #
    #     def get(self, request, pk, format=None):
    #         snippet = self.get_object(pk)
    #         serializer = SnippetSerializer(snippet)
    #         return Response(serializer.data)


# class AuthorDetail(APIView):
#     def get_author(self, pk):
#         try:
#             return Author.objects.get(pk=pk)
#         except Author.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         queryset = self.get_author(pk)
#         serializer = AuthorSerializer(queryset)
#         return Response(serializer.data)


class GetAllBooks(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def author_name(request, pk):


#     if request.method == 'GET':
#         queryset = Author.objects.get(pk=pk)
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(queryset)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class GetBookById(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = 'id'


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.select_related('author').all()
#     serializer_class = BookSerializer


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class GetAllAuthors(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    message = 'smile is sleeping in class, bcos her code is not running'
    subject = 'smile must do django'
    send_mail(subject, message, '', ['smileokuta3@gmail.com'])
    return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookAuthorView(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'genre']
    search_fields = ['language', 'price']

    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
