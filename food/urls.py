from django.urls import path
from .views import index, food_place_list,    add_comment, blog, toggle_favorite, favorites,  FoodPlaceDetailView , food_list
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('food_place_list', views.food_place_list, name='food_place_list'),
    path('foodplace/<int:pk>/', FoodPlaceDetailView.as_view(), name='food_detail'),
    path('add_comment/<int:food_id>/', views.add_comment, name='add_comment'),
    path('blog/<int:food_id>/', views.blog, name='blog'),
    path('add_comment/<int:food_id>/', views.add_comment, name='add_comment'),
    path('toggle_favorite/', toggle_favorite, name='toggle_favorite'),
  
    path('food-list/', views.food_list, name='food_list'),
    # path('food_place_detail/', views.food_place_detail, name='food_place_detail'),
    # path('', FoodPlaceListView.as_view(), name='FoodPlaceView'),
    # path('foodplace/<int:id>/', views.food_detail, name='food_detail'),
    
]