from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)
   
    
    def __str__(self):
        return self.user.username
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class FoodPlace(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='place_pics', blank=True)
    adress = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    adress = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
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
    


