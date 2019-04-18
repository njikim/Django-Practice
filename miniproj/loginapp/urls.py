from django.urls import path
from loginapp import views

urlpatterns = [
    path('', views.login),
    path('main', views.main),
    path('call_main', views.call_main),
    path('shop', views.shop),
]