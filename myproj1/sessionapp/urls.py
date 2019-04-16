from django.urls import path
from sessionapp import views

urlpatterns = [
    path("", views.main),
    path("setOS", views.setOS),
    path("showOS", views.showOS),
]