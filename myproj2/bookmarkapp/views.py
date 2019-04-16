from django.shortcuts import render
from bookmarkapp.models import Bookmark

# Create your views here.
def mainFunc(request):
    Bookmark.objects.all()
    urlCount = Bookmark.objects.all().count()
    return render(request, 'home.html', {'urlCount': urlCount})
