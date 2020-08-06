from django.urls import path
from . import views

urlpatterns = [
    path('answer', views.answer, name = "answer"),
    path('document', views.document, name = "document"),
    path('', views.home, name = "home"),
]