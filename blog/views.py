from django.shortcuts import render # used to render templates. 
from .models import Post # allows the views to interact with the database through the model

# Define a view function for the home page
def home(request):
    # Retrieve all Post objects from the database
    # and store them in the 'posts' variable in the context dictionary
    context = {
        'posts': Post.objects.all()
    }
    
    # Render the home.html template with the provided context
    return render(request, 'blog/home.html', context)

# Define a view function for the about page
def about(request):
    # Render the about.html template with a context containing the 'title' variable
    return render(request, 'blog/about.html', {'title': 'About'})
