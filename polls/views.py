from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'polls/index.html',context)
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

