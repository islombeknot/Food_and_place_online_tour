from django.shortcuts import render ,  redirect, reverse 
from django.contrib.auth.models import User
from .models import Profile
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            
            if user is not None:
                return redirect('index')
        return render(request, 'index.html', {'form': form})
    
class login_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already authenticated.")
            return redirect('index')  
          
        form = LoginForm()
        return render(request, 'users/login.html', context={"form":form})
     
    def post(self, request):
          form = LoginForm(request.POST)
          if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user = authenticate(username=username, password=password)
               if user is not None:
                    login(request, user)
                    return redirect("login")
          return render(request, 'index.html',context={"form":form})



class LogoutView(LoginRequiredMixin, View):
  def get(self, request):
      logout(request)

      return redirect('login')
  
