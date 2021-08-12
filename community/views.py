from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .forms import newJogging, newCare
from .models import newJogging, newCare
# Create your views here.

def home(request):
    return render(request, 'community/home.html')

def new(request):
    return render(request, 'community/new.html')

def createJogging(request, jog_id):
    joggingobject = get_object_or_404(newJogging, pk=jog_id)
    if request.method=="POST":
        form=newJogging(request.POST)
        if form.is_valid():
            form.save()
            return redirect('readJogging', jog_id)    
    else:
        form=newJogging()
        return render(request, 'community/createJogging.html', {'form':form})


def createCare(request):
    form = newCare()
    return render(request, 'community/createCare.html', {'form':form})


def readJogging(request):
    jog = newJogging.objects
    return render(request, 'community/readJogging.html', {'jogs':jog})


def readCare(request):
    care = newCare.objects
    return render(request, 'community/readCare.html', {'cares':care})


def detailJogging(request, jog_id):
    joggingobject = get_object_or_404(newJogging, pk=jog_id)
    return render(request, 'community/detailJogging.html', {'joggingobject':joggingobject})

