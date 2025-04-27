from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddMenuForm, AddCategoryForm, OfferForm
from .models import Food, Category, Offer
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def food_view(request):
    if not request.user.is_superuser:
        return redirect('profile')
    
    foods = Food.objects.all()
    categories = Category.objects.all()

    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'menuapp/foods.html', context)

@login_required
def add_food(request):
    if not request.user.is_superuser:
        return redirect('profile')
    
    if request.method == 'POST':
        form = AddMenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddMenuForm()
    return render(request, 'menuapp/addmenu.html', {'form': form})

@login_required
def edit_food(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = AddMenuForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddMenuForm(instance=food)
    return render(request, 'menuapp/addmenu.html', {'form': form})

@login_required
def delete_food(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('foods')

@login_required
def add_categories(request):
    if not request.user.is_superuser:
        return redirect('profile')
    
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddCategoryForm()
    return render(request, 'menuapp/addcategory.html', {'form': form})

@login_required
def edit_categories(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddCategoryForm(instance=category)
    return render(request, 'menuapp/addcategory.html', {'form': form})

@login_required
def delete_categories(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('foods')

@login_required
def offer_view(request):
    if not request.user.is_superuser:
        return redirect('profile')
    
    offers = Offer.objects.all()
    context = {
        'offers': offers
    }
    return render(request, 'menuapp/offer.html', context)

@login_required
def create_offer_form(request):
    if not request.user.is_superuser:
        return redirect('profile')
    
    if request.method == "POST":
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.save()
            form.save_m2m()
            return redirect('offers')
    form = OfferForm()
    return render(request, "menuapp/offerform.html", {'form': form})

@login_required
def edit_offer(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    offer = get_object_or_404(Offer, pk=pk)
    if request.method == "POST":
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            offers = form.save(commit=False)
            offers.save()
            form.save_m2m()
            return redirect('offers')
    form = OfferForm(instance=offer)
    return render(request, "menuapp/offerform.html", {'form': form})

@login_required
def delete_offer(request, pk):
    if not request.user.is_superuser:
        return redirect('profile')
    
    offer = get_object_or_404(Offer, pk=pk)
    offer.delete()
    return redirect('offers')
