from django.shortcuts import render, get_object_or_404

from menuapp.models import Food, Offer

# Create your views here.
def home(request):
    foods = Food.objects.all()
    offers = Offer.objects.all().order_by('-id')
    context = {
        'foods': foods,
        'offers': offers,
    }
    return render(request, 'myapp/index.html', context)