from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('aboutus/', views.show_about_page, name="about us"),
    path('', views.show_home_page, name="home page"),
    path('/category/<int:cid>', views.category_page, name="category page"),
]
