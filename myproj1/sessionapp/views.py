from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def main(request):
    return render(request, 'main.html')

def setOS(request): # favorite_os의 값 유무에 따라 return값을 다르게
    if "favorite_os" in request.GET:
        os = request.GET.get("favorite_os") 
        request.session['f_os'] = os        # 세션 생성 (값을 오래 저장 가능)
        print('showOS 함수 불러오기 직전')
        return HttpResponseRedirect("showOS1")   # setOS 요청값 처리
    else:
        return render(request, 'setOS.html')    # main 요청값 처리


def showOS1(request):
    print('showOS1 함수 불러온 직후')
def showOS(request):    
    print('showOS 함수 불러온 직후')
    if "f_os" in request.session:
        request.session.set_expiry(3)
        return render(request, 'showOS.html', {"os":request.session["f_os"]})
    else:
        return render(request, "showOS.html", {"os": "선택한 os가 없습니다."})




'''
def setOS(request):
    return render(request, 'setOS.html')

def showOS(request):
    os = request.GET.get("favorite_os")   
    return render(request, 'showOS.html', {"os":os})
'''