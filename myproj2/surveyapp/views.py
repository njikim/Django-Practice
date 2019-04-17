from django.shortcuts import render
from surveyapp.models import Survey, Answer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    dto = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, 'survey_home.html', {"dto":dto})

@csrf_exempt
def save_survey(request):
    idx = request.POST["idx"]
    num = request.POST["num"]
    Answer(survey_idx=idx, num=num).save()
    return render(request, 'success.html')