from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.

def welcome(request):

    return render(request,"website/welcome.html",{"message":"This is the welcome page rendered" ,"number_of_meetings":Meeting.objects.count(),'meeting':Meeting.objects.all})

