from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddMenuForm, AddCategoryForm
from .models import Food, Category

# Create your views here.
def food_view(request):
    foods = Food.objects.all()
    categories = Category.objects.all()

    context = {
        'foods': foods,
        'categories': categories,
    }
    return render(request, 'menuapp/foods.html', context)

def add_food(request):
    if request.method == 'POST':
        form = AddMenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddMenuForm()
    return render(request, 'menuapp/addmenu.html', {'form': form})

def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = AddMenuForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddMenuForm(instance=food)
    return render(request, 'menuapp/addmenu.html', {'form': form})

def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('foods')

def add_categories(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddCategoryForm()
    return render(request, 'menuapp/addcategory.html', {'form': form})

def edit_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("foods")
    else:
        form = AddCategoryForm(instance=category)
    return render(request, 'menuapp/addcategory.html', {'form': form})

def delete_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('foods')

