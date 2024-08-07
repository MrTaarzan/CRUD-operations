from django.db import models


# Create your models here.
class FoodName(models.Model):
    food_category = (
        ('VEG', 'VEG'),
        ('NON VEG', 'NON VEG')
    )
    Name = models.CharField(max_length=30)
    Price = models.IntegerField()
    Category = models.CharField(max_length=20, choices=food_category)
