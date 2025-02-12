from django.urls import path
from .import views

urlpatterns = [
    path('profile/', views.profile_view, name="profile"),
    path('ceate-account/', views.resiter_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]