from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect

# Create your views here.
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def main(request):
    if "id" in request.POST:
        user_id = request.POST["id"]
        user_pw = request.POST["pw"]
        request.session["sess_id"] = user_id
        return HttpResponseRedirect("call_main") 
    else:
        return render(request, 'error.html')

@csrf_exempt
def call_main(request):
    if "sess_id" in request.session:
        id = request.session["sess_id"]
        return render(request, 'main.html', {"id": id})

def shop(request):
    return render(request, 'shop.html')

