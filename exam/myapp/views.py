from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):     
    return HttpResponse("안녕하세요")

def hello_template(request):
    return render(request, 'hello.html')