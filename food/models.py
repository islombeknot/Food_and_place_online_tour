from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


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
    category = models.ForeignKey(Category,related_name=('cat'), on_delete=models.CASCADE)
    favorite_users = models.ManyToManyField(User, related_name='favorite_food_places')

    @classmethod
    def sorted_by_category(cls):
        return cls.objects.order_by('category__name', 'name')

    def __str__(self):
        return self.name
    

class Food(models.Model):
    food_id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    place = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=1)
    image = models.ImageField(upload_to='meal_pics', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    stars_given = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])

    def __str__(self):
        return self.name
    
   
class FoodComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    foodplace = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment
    
class FavoriteFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
    


