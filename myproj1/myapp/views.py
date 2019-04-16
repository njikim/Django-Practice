from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):     # 사용자가 접속 시 (요청 시) 함수 호출됨
    return HttpResponse("인덱스 요청 처리. 여기는 메인 페이지")

def hello(request):
    msg = '장고하이'
    ss = "<html><body>장고 프젝 구현 %s </body></html>"%(msg)   
    return HttpResponse(ss)

def hello_template(request):
    name = '은지'
    return render(request, 'hello.html', {'name':name})

def hello_images(request):
    return render(request, 'image.html')