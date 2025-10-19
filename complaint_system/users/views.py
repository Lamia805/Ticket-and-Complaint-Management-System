from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages 
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message to be displayed on the next page
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

