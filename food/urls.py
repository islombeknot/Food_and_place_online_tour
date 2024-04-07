from django.urls import path
from .views import index, food_place_list,  FoodPlaceDetailView,  add_comment, blog
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('food_place_list', views.food_place_list, name='food_place_list'),
    path('foodplace/<int:pk>/', FoodPlaceDetailView.as_view(), name='food_detail'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('blog/<int:food_id>/', views.blog, name='blog'),
    # path('', FoodPlaceListView.as_view(), name='FoodPlaceView'),
    # path('foodplace/<int:id>/', views.food_detail, name='food_detail'),
    # path('add_comment/<int:food_id>/', AddCommentView.as_view(), name='add_comment'),
]