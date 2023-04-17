from django.urls import path, include
from rest_framework.routers import SimpleRouter, SimpleRouter
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('book_instance', views.BookInstanceViewSet)


urlpatterns = [
    # path('book/', views.BookCreateApiView.as_view()),
    path('', include(router.urls)),
    path('createbook/', views.BookCreateView.as_view()),
    path('bookauthor', views.BookAuthorView.as_view()),
    path('author/<int:pk>/', views.author_detail, name='author-detail'),
    # path('books/', views.BookListApiView.as_view()),
    path('book/<int:id>/', views.GetBookById.as_view()),
    path('createauthor/', views.AuthorCreateView.as_view()),
    path('authors/', views.GetAllAuthors.as_view()),

    # path('book/<int:pk>/', views.book_details, name='book_list'),
    # path('authors/', views.author_details, name='authors'),
    # path('authors/<int:pk>/', views.author_name, name='author')
]
