from django.shortcuts import render

# Create your views here.

from .models import Question, Choice

#Get question and displayssd

def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
