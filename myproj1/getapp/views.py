from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mainFunc(request):
    return render(request, 'index.html')

class CallView(TemplateView):
    template_name = "callget.html" # template_name는 장고 default 변수

def insertFunc(request):
    return render(request, "insert.html")
