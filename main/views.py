from django.shortcuts import render
from .models import *
from .chatbot import answer_of_query

# Create your views here.
def home(request):
    return render(request, "home.html")

def answer(request):
    q = request.GET['question']
    question_obj = queries()
    question_obj.question = q
    ans = answer_of_query(str(q))
    question_obj.answer = ans
    question_obj.save()

    return render(request, "answer.html", {"question" : q, "answer" : ans})

def document(request):
    return render(request, "document.html")