# from django.shortcuts import render
# from bookmarkapp.models import Bookmark

# # Create your views here.
# def mainFunc(request):
#     Bookmark.objects.all()
#     urlCount = Bookmark.objects.all().count()
#     return render(request, 'home.html', {'urlCount': urlCount})


from django.shortcuts import render
from bookmarkapp.models import Bookmark

# Create your views here.
def home(request):
    urlCount = Bookmark.objects.all().count()
    urlList = Bookmark.objects.order_by("title")
    return render(request, 'home.html', {"urlCount": urlCount, 'urlList':urlList})
    #return render(request, 'home.html')