from django.shortcuts import render

# Create your views here.

from .models import Question,Choice

#Get question and displays

def index(request):
    return render(request, 'polls/index.html')
