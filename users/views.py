from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import RegisterForm, LoginForm


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already authenticated.")
            return redirect('index')

        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'users/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already authenticated.")
            return redirect('index')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'index.html', {'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')
    
class ProfileView(View):
    def get(self, request):
        return render(request, 'users/profile.html')

  

def profile(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'paswordingiz muvaffaqiyatli ozgartirildi')
            return redirect('profile')
        else:
            messages.error(request, 'iltimos xatolikni togirlang')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/profile.html', {'form': form})