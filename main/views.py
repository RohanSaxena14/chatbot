from django.shortcuts import render
from .models import *
from .chatbot import give_me_answer

# Create your views here.
def home(request):
    return render(request, "home.html")

def answer(request):
    q = request.GET['question']
    question_obj = queries()
    question_obj.question = q
    ans = give_me_answer(q)
    question_obj.answer = ans
    question_obj.save()

    return render(request, "answer.html", {"question" : q, "answer" : ans})

def document(request):
    return render(request, "document.html")