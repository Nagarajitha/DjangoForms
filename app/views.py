from django.shortcuts import render
from django.http import HttpResponse

from app.forms import *

# Create your views here.

def student(request):
    #empty student form object
    ESFO = StudentForm()
    d = {'ESFO':ESFO}

    if request.method == 'POST':
        #Student Form Data Objest
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            print(SFDO.cleaned_data)
        else:
            return HttpResponse('Invalid Data')
    return render(request,'student.html',d)


def topic(request):
    #empty topic form object
    ETFO =TopicForm()

    d = {'ETFO':ETFO}
    
    if request.method == 'POST':
        #Topic Form Data Objest
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            print(TFDO.cleaned_data)
        else:
            return HttpResponse('Invalid Data')
    return render(request,'topic.html',d)



    





