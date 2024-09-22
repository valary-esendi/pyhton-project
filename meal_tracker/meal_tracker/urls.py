"""
URL configuration for meal_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from meals import views  # Ensure views are imported from your meals app
from meals.views import register,CustomLoginView, logout_view, meals_view
from django.views.generic.base import TemplateView  # Import TemplateView if needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout_view'),
    path('meals/', meals_view, name='meals'),
    path('', TemplateView.as_view(template_name='meals/home.html'), name='home'),  # Optional: Home Page view
    path('accounts/', include('django.contrib.auth.urls')),  # Optional: Include Django's built-in auth views
]

