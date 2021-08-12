from django.contrib import auth
from django.contrib.auth.forms import UsernameField
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from account.forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'community/home.html')

# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)  # 사용자 인증
#             login(request, user)  # 로그인
#             return redirect('home')
#     else:
#         form = UserForm()
#     return render(request, 'account/signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'account/signup.html')


