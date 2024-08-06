from django.db import models


# Create your models here.
class FoodName(models.Model):
    food_category = (
        ('veg', 'veg'),
        ('non', 'non veg')
    )
    Name = models.CharField(max_length=30)
    Price = models.IntegerField()
    category = models.CharField(max_length=20, choices=food_category)
