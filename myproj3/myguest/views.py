from django.shortcuts import render
from myguest.models import Guest
# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    gdata = Guest.objects.all()
    return render(request, 'list.html', {'gdatas': gdata})