from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import newJogging, newCare, commentJogging
from .forms import newJoggingform, newCareform, commentJoggingform
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.

def home(request):
    return render(request, 'community/home.html')

def new(request):
    return render(request, 'community/new.html')


@login_required(login_url='account:login')
def createJogging(request):
    if request.method=="POST":
        form=newJoggingform(request.POST)
        if form.is_valid():
            createjog = form.save(commit=False)
            createjog.author = request.user
            createjog.image = request.FILES['image']
            form.save()
            return redirect('readJogging')    
    else:
        form=newJoggingform()
        return render(request, 'community/createJogging.html', {'form':form})


def createCare(request):
    form = newCareform()
    return render(request, 'community/createCare.html', {'form':form})


def readJogging(request):
    jog = newJogging.objects.all()
    return render(request, 'community/readJogging.html', {'jogs':jog})


def readCare(request):
    care = newCare.objects.all()
    return render(request, 'community/readCare.html', {'cares':care})


def detailJogging(request, jog_id):
    joggingobject = get_object_or_404(newJogging, pk=jog_id)
    return render(request, 'community/detailJogging.html', {'joggingobject':joggingobject})



@login_required(login_url='account:login')
def commentJog(request, jog_id):
    jog = get_object_or_404(newJogging, pk=jog_id)

    if request.method == "POST":
        form = commentJoggingform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = jog
            comment.author = request.user
            comment.save()
            return redirect('detailJogging', jog_id)
    else:
        form=commentJoggingform()
        return render(request, 'community/commentJogging.html', {'form':form})
        


