from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="food")
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    avaiable = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Offer(models.Model):
    foods = models.ManyToManyField(Food, related_name="foods")
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    offer_persentage = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    last_date = models.DateTimeField(null=True, blank=True)

    def total_price(self):
        return sum(food.price for food in self.foods.all())

    def less_price(self):
        total = self.total_price()
        return ((total*self.offer_persentage) // 100)
    
    def final_price(self):
        return (self.total_price() - self.less_price())
    
    def duration(self):
        if self.start_date and self.last_date:
            return self.last_date - self.start_date
        return timedelta(0)  # Default if dates are missing

    def formatted_duration(self):
        duration = self.duration()
        days = duration.days
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        if days > 0:
            return f"{days} days, {hours} hours, {minutes} minutes"
        return f"{hours} hours, {minutes} minutes"

    def __str__(self):
        return self.title