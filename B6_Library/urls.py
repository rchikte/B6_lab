"""B6_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from unicodedata import name
from os import name
from django.contrib import admin
from django.urls import path
# from Book.views import homepage, show_all_books, new_book_entry, edit_data
# from Book.views import *
from Book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="homepage"),
    path('show-all-books/', views.show_all_books, name="show_all_books"),
    path('new_book_entry/', views.new_book_entry, name="new_book_entry"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('buy_book/', views.buy_book, name="buy_book"),
    path('address_email/', views.address_email, name="address_email"),
    path('delete_all/', views.delete_all, name="delete_all"),
    path('proceed_to_buy/', views.proceed_to_buy, name="proceed_to_buy"),
    path('non_active_book/', views.non_active_book, name="non_active_book"),
    path('soft_delete_book/<int:id>/', views.soft_delete_book, name="soft_delete_book"),
    path('restore_book/<int:id>/', views.restore_book, name="restore_book"),

   
  
]
