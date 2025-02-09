from django.db import models

# Create your models here.
class Category(models.Model):
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