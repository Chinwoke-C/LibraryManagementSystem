
from django.urls import path, include

from book import views

urlpatterns = [
    path('email/', views.playground),
]