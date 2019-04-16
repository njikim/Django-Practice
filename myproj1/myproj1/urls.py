"""myproj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views
from getapp import views
from getapp.views import CallView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # myapp 접속 경로
    path('', include('myapp.urls')),    # include: 접속 경로 toss
    
    # getapp 접속 경로
    path('getapp/', views.mainFunc),     # 바로 views에 있는 함수 불러옴
    path('getapp/callget', CallView.as_view()),
    path('getapp/', include('getapp.urls')),

    # sessionapp 접속 경로
    path('sessionapp/', include('sessionapp.urls')),

    # dbapp 접속경로
    path('dbapp/', include('dbapp.urls')),
]

