from django.shortcuts import render, get_object_or_404
from menuapp.models import Food

# Create your views here.
def home(request):
    food = Food.objects.all()
    context = {
        'foods': food,
    }
    return render(request, 'myapp/index.html', context)
