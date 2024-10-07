import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_tracker.settings')  # Ensure correct settings module
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Meal 
from django.views import View
from .forms import MemberForm
from .models import Member
from .forms import MealForm
from django.contrib import messages  # Import messages for feedback

# Registration View
def register(request):
    print("Register view hit.")
    if request.method == 'POST':
        print("Processing POST request for registration.")

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            print(f"User {user.username} registered successfully.")
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Registration successful! Welcome!')
            return redirect('meals')  # Redirect to meals page after registration
        else:
            print("Form is invalid. Errors found:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        print("GET request for registration form.")
        form = UserCreationForm()  # Create a blank form for GET request
    
    return render(request, 'meals/register.html', {'form': form})

# Custom Login View
class CustomLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        print("GET request for login view.")
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("Processing POST request for login.")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"User {user.username} logged in successfully.")
            messages.success(request, 'Login successful!')
            return redirect('meals')
        else:
            print("Login failed. Invalid credentials.")
            messages.error(request, 'Invalid credentials. Please try again.')
        return render(request, self.template_name, {'form': form})

# Logout View
def logout_view(request):
    print("Logging out user.")
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')  # Redirect to login page after logout


# Meals View
def meals_view(request):
    if request.user.is_authenticated:
        print(f"User {request.user.username} accessed meals view.")
        
        # Handling the meal addition
        if request.method == 'POST':
            form = MealForm(request.POST)
            if form.is_valid():
                meal = form.save(commit=False)
                meal.user = request.user  # Associate the meal with the logged-in user
                meal.save()
                messages.success(request, 'Meal added successfully!')
                return redirect('meals')  # Redirect to the meals page after adding

        else:
            form = MealForm()  # Create a blank form for GET request

        # Get all meals for the logged-in user
        meals = Meal.objects.filter(user=request.user)  # Fetch meals associated with user

        return render(request, 'meals/meals.html', {
            'form': form, 
            'meals': meals  # Pass the meals to the template
        })
        
    else:
        print("Unauthorized access attempt to meals view. Redirecting to login.")
        return redirect('login')  # Redirect to login if not authenticated
    

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('/membersList')  # Redirect to a success page after submission
    else:
        form = MemberForm()
    
    return render(request, 'main/addMember.html', {'form': form})

# View to display the list of members
def members_list(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'main/membersList.html', {'members': members})