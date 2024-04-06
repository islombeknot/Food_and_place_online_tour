from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class FoodPlace(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='place_pics', blank=True)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    image = models.ImageField(upload_to='meal_pics', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
   
class FoodComment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
class FavoriteFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
