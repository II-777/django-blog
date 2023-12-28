"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# Import the admin module for Django's administration site
from django.contrib import admin
# Import functions for defining URL patterns
from django.urls import path, include
# Import the 'register' view from the 'users' app's views module and alias it as 'user_views'
from users import views as user_views

# Define URL patterns for the Django project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # Include URL patterns from the 'blog' app
    path('', include('blog.urls')),
    # User registration URL, mapped to the 'register' view
    path('register/', user_views.register, name='register'),
]