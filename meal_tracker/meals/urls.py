from django.urls import path
from .views import register, custom_login, logout_view, meals_view
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add-member/', views.add_member),
    path('membersList/', views.members_list),
    path('', meals_view, name='meals'),  # Make sure you have a default route for meals
]