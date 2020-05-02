from django.shortcuts import render, get_object_or_404,redirect
from .models import Meeting, Room
#from django.forms import modelform_factory
from . forms import MeetingForm

# Create your views here.

#MeetingForm=modelform_factory(Meeting, exclude=[])
def detail(request,id):
        meeting=get_object_or_404(Meeting,pk=id)
        return render(request,"meeting/detail.html",{"meeting":meeting})

def rooms(request):
        # room=get_object_or_404(Room,pk=id)
        return render(request,"meeting/rooms.html",{"room":Room.objects.all})

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm
    return render(request,"meeting/new.html",{'form':form})