from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search_blog, name='search_blog'),
    path('', blog, name='blog'),
    path('create/', create_blog, name='create_blog'),
    path('myblog/', my_blog, name='my_blog'),
    path('<str:slug>/update', update_blog, name='update_blog'),
    path('<str:slug>/delete/', delete_blog, name='delete_blog'),
    path('<str:slug>/', details_blog, name='details_blog'),
]