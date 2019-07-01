from django.shortcuts import render
from bookmarkapp.models import Bookmark

# Create your views here.
def home(request):
    urlCount = Bookmark.objects.all().count()
    urlList = Bookmark.objects.order_by("title")
    return render(request, 'home.html', {"urlCount": urlCount, "urlList":urlList})
    # return render(request, 'home.html')

def detail(request):
    addr = request.GET["url"]

    # select * from bookmark_bookmark where url=http://www.google.com
    dto = Bookmark.objects.get(url=addr)            # 넘겨줄 데이터가 많은 경우 이런식으로!!!!!!!!!!
    print(dto.title , ',' , dto.url)
    return render(request, 'detail.html', {"dto": dto})


'''
def detail(request):
    addr = request.GET["url"]
    return render(request, 'detail.html', {"addr":addr})
'''