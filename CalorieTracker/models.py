from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

class Consume(models.Model):
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
