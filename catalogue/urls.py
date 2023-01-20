from django.views.generic import RedirectView
from django.urls import path, include

from catalogue import views

urlpatterns = [

    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorListView.as_view(), name='author-detail'),



]
