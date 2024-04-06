from django.urls import path
from . import views 
from .views import RegisterView, login_view, LogoutView

app_name = 'users'

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', login_view.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
]