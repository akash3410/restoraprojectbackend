from django.shortcuts import render, get_object_or_404

from menuapp.models import Food, Offer

# Create your views here.
def home(request):
    foods = Food.objects.all()
    offers = Offer.objects.all()
    context = {
        'foods': foods,
        'offers': offers,
    }

# Create your views here.
def home(request):
    food = Food.objects.all()
    context = {
        'foods': food,
    }
    return render(request, 'myapp/index.html', context)
