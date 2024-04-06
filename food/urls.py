from django.urls import path
from .views import index, food_place_list, FoodPlaceDetailView
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    # path('', FoodPlaceListView.as_view(), name='FoodPlaceView'),
    path('food_place_list', views.food_place_list, name='food_place_list'),
    path('foodplace/<int:pk>/', FoodPlaceDetailView.as_view(), name='food_detail'),
]