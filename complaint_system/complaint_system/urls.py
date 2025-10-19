"""
URL configuration for complaint_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs for ticket management.
    # The first line inside 'tickets.urls' should define the root path ('') 
    # for the dashboard. The view for the dashboard is protected, so this setup
    # will automatically redirect any unauthenticated user to your login page.
    path('', include('tickets.urls')),
    
    # URLs for user authentication (login, logout, register).
    path('', include('users.urls')),
    
    # URLs for complaint management.
    path('', include('complaints.urls')),
]

