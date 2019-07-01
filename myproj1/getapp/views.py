from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mainFunc(request):
    return render(request, 'index.html')

class CallView(TemplateView):
    template_name = "callget.html" # template_name: 장고 default 변수

def insertFunc(request):
    # print('요청 방식:' + request.method)
    if request.method == 'GET':     # 요청방식 check 가능
        print('get 요청 처리')
        return render (request, "insert.html")
    else:
        name = request.POST.get("name")
        return render(request, "list.html", {"name": name})
