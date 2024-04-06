from django.contrib import admin
from .models import FoodPlace, Food, Category, FoodComment, FavoriteFood

# Register your models here.

admin.site.register(Category)
admin.site.register(FoodPlace)
admin.site.register(Food)
admin.site.register(FoodComment)
admin.site.register(FavoriteFood)