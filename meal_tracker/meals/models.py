from django.db import models
from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import User

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=100)  # e.g., 'Protein', 'Fat'
    times_consumed = models.IntegerField(default=0)
    food_expiration = models.DateField()

    def __str__(self):
        return self.meal_name

#member model
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"