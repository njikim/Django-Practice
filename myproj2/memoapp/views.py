from django.shortcuts import render, redirect
from memoapp.models import Memo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    memoList = Memo.objects.order_by("-idx")       #내림차순 정렬, 최신글이 맨 위로
    memoCount = Memo.objects.all().count()
    return render(request, 'list.html', {"memoList": memoList, "memoCount": memoCount})


@csrf_exempt    #POST 방식 사용 시
def insert(request):
    writer = request.POST["writer"]
    memo = request.POST["memo"]
    print(writer, ',', memo)
    # 테이블에 데이터 저장
    Memo(writer=writer, memo=memo).save()
    # 리스트 페이지로 복귀
    #return render(request, 'list.html')     
    return redirect("/memolist")                       # home함수가 호출 돼야 데이터가 저장됨

def detail(request):
    idx = request.GET["idx"]
    dto = Memo.objects.get(idx=idx)
    return render(request, 'memodetail.html', {"dto": dto})

def delete(request):
    idx = request.GET["idx"]
    Memo.objects.get(idx=idx).delete()
    return redirect("/memolist")                    # 삭제 후, home함수 호출되야함.

@csrf_exempt
def update(request):
    # update table명 set writer=writer, memo=memo where idx=idx
    writer = request.POST["writer"]
    memo = request.POST["memo"]

    ## 중요!!!! html에서 input type="hidden"으로 설정. otherwise 값 안넘어옴.
    idx = request.POST["idx"]           
    Memo(idx=idx, writer=writer, memo=memo).save()
    return redirect("/memolist")