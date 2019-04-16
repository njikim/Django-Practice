from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),          #http://127.0.0.1:8000/
    path('hello', views.hello),     #http://127.0.0.1:8000/hello
    path('hello_tem', views.hello_template),
    path('img', views.hello_images),
]

