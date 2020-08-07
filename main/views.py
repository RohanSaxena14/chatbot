from django.shortcuts import render
from .models import *
from .chatbot import answer_of_query

# Create your views here.
def home(request):
    all_queries = []
    if 'question' in request.GET:
        q = request.GET['question']
        if q.lower() == "delete my chat":
            start = True   
            try:
                queries.objects.all().delete()
            except:
                pass
        else:
            question_obj = queries()
            question_obj.question = q
            ans = answer_of_query(str(q))
            question_obj.answer = ans
            question_obj.save()
            start = False
        
        all_queries = queries.objects.all()
        
    else :
        start = True
        
    return render(request, "home.html", {"queries" : all_queries, "start" : start})