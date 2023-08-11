from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('create/', create, name='create'),
    path('<str:slug>/update', update, name='product_update'),
    path('<str:slug>/delete/', delete, name='product_delete'),
    path('<str:slug>/', details, name='details'),
    path('',shop ,name='shop')
]