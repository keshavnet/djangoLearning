from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question

# Create your views here.


def index(req):
    latest_question_list = Question.objects.order_by('pub_date')[:5]

    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context, req))
    return render(req, 'polls/index.html', context)


def detail(req, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    print('detail ', question)
    return render(req, 'polls/detail.html', {'question': question})


def results(req, question_id):
    response = "<b>You're looking at result of question %s.</b>"
    return HttpResponse(response % question_id)


def vote(req, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
