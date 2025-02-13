from django import forms
from .models import Food, Category, Offer

class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'category name'})
    )

    is_active = forms.BooleanField(
        label='Active Status',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )

    class Meta:
        model=Category
        fields=['name', 'is_active']

class AddMenuForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
        max_length=20
    )
    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Food Description'}),
        max_length=100
    )
    price = forms.IntegerField(
        label="Price",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Food Price'})
    )
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Food Categories",
        empty_label='Select a Category',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    avaiable = forms.BooleanField(
        label="Available",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )
    image = forms.ImageField(
        label="Upload Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Food
        fields = ['title', 'description', 'price', 'categories', 'avaiable', 'image']


class OfferForm(forms.ModelForm):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Name'}),
    )
    description = forms.CharField(
        label="Description",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Description'}),
        max_length=150
    )
    foods = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        label="Select Food",
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Food Name'}),
    )
    offer_persentage = forms.CharField(
        label="Offer Amount (%)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: 20'}),
    )
    start_date = forms.DateTimeField(
        label="Start Date",
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'mm:dd:yyyy', 'type': 'datetime-local'}),
    )
    last_date = forms.DateTimeField(
        label="End Date",
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'mm:dd:yyyy', 'type': 'datetime-local'}),
    )

    class Meta:
        model = Offer
        fields = ['title', 'description', 'foods', 'offer_persentage', 'start_date', 'last_date']