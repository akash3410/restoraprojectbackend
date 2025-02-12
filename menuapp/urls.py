from django.urls import path
from .import views

urlpatterns = [
    path('foods/', views.food_view, name='foods'),
    path('add-food/', views.add_food, name='addfood'),
    path('edit-food/<int:pk>', views.edit_food, name='editfood'),
    path('delete-food/<int:pk>', views.delete_food, name='deletefood'),
    path('add-categories/', views.add_categories, name='addcategories'),
    path('edit-categories/<int:pk>', views.edit_categories, name='editcategories'),
    path('delet-categories/<int:pk>', views.delete_categories, name='deletecategories'),
    path('offers/', views.offer_view, name='offers'),
    path('create-offer/', views.create_offer_form, name='createoffer'),
    path('edit-offer/<int:pk>', views.edit_offer, name='editoffer'),
    path('delete-offer/<int:pk>', views.delete_offer, name='deleteoffer'),
]