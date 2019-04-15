from django.urls import path
from getapp import views

urlpatterns = [
    path('insert', views.insertFunc)
]