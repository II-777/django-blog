# Django Blog

## Part 1 - Getting Started
1. Run the following commands:
```bash
# To create and start python3 virtual environment 
py -m venv .venv
source .venv/bin/activate
# To install required python3 modules 
pip install -r requirements.txt
# To create a new django project
django-admin startproject django_project
```

### The `startproject` command cretes the following django file structure:
- new file:   django_project/__init__.py
- new file:   django_project/settings.py
- new file:   django_project/urls.py
- new file:   django_project/wsgi.py
- new file:   manage.py
- new file:   db.sqlite3

### Note: 
1. **`django_project/__init__.py`:**
   - This file is an empty Python script that tells Python that the directory should be considered a Python package. It is typically left blank unless you have specific initialization code for the package.
2. **`django_project/settings.py`:**
   - The primary configuration file for a Django project, containing settings such as database configuration, static files, middleware, and other project-specific configurations.
3. **`django_project/urls.py`:**
   - Defines the URL patterns for the project, mapping URLs to views. It serves as the central routing mechanism for directing incoming requests to the appropriate view functions.
4. **`django_project/wsgi.py`:**
   - Stands for Web Server Gateway Interface. This file serves as an entry point for the WSGI server to interact with your Django application, enabling it to be deployed on production servers.
5. **`manage.py`:**
   - A command-line utility that provides various tools for interacting with and managing a Django project, including running development servers, creating database tables, and handling migrations.
6. **`db.sqlite3`:**
   - The default SQLite database file created by Django when you run migrations. It stores the project's data, including tables for models defined in the project's apps. This file is part of the default configuration and can be replaced with other database backends as needed.

## Part 2 - Applications and Routes
1. Run the following command:
```bash
# To create a django app
py manage.py startapp blog
```
### The `startapp` command cretes the following django file structure: 
- new file:   blog/__init__.py
- new file:   blog/admin.py
- new file:   blog/apps.py
- new file:   blog/migrations/__init__.py
- new file:   blog/models.py
- new file:   blog/tests.py

2. Modify `django_project/settings.py` to register the new app `blog`
```python
# django_project/settings.py
INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

3. Create views for `home page` and `about page`
```python
# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

4. Create **app-level routes** for `home page`, `blog page` and `about page`
```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
```

5. Create **project-level routes** for `home page`, `blog page` and `about page`
```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

## Part 3 - Templates
### Add templates and static files: 
- new file:   blog/static/blog/main.css
- new file:   blog/templates/blog/about.html
- new file:   blog/templates/blog/base.html
- new file:   blog/templates/blog/home.html

1. Modify `blog/views.py` to display html templates
```python
# blog/views.py
# module used to render html templates
from django.shortcuts import render

# Sample data representing blog posts (later to be replaced with database queries)
posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "December 14, 2023",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "December 15, 2023",
    },
]

# Define a view function for the home page
def home(request):
    # Create a context dictionary with the sample blog posts
    context = {"posts": posts}
    
    # Render the home.html template with the provided context
    return render(request, "blog/home.html", context)

# Define a view function for the about page
def about(request):
    # Render the about.html template with a context containing the 'title' variable
    return render(request, "blog/about.html", {"title": "About"})
```

## Part 4 - Admin Page
```bash
# Create database migration files based on changes in the models
py manage.py makemigrations
# Apply pending database migrations to update the database schema
py manage.py migrate
# Create a superuser account for administrative purposes
py manage.py createsuperuser
```

### Now you can login, using the superuser credentials via:
```bash
http://127.0.0.1:8000/admin/
```

## Part 5 - Database and Migrations
### Links:
- [Djangoproject Documentation Models](https://docs.djangoproject.com/en/3.2/topics/db/models/)
- [Djangoproject Documentation Templates Date](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#date)

### Changes made:
- modified:   blog/views.py
- modified:   blog/models.py
- new file:   blog/migrations/0001_initial.py
- modified:   blog/templates/blog/home.html
- modified:   blog/admin.py

1. Modify `blog/models.py` file to display database data
```python
# blog/models.py
from django.db import models # working with Django models
from django.utils import timezone # handling timezones 
from django.contrib.auth.models import User # integrating user authentication  
"""
Imports: 
1. models is a part of Django's Object-Relational Mapping (ORM) system, and 
it provides classes and functions to define and interact with database models. 
2. timezone module provides utilities related to handling time zones in Django applications. 
In this case, it's used to set the default value for the date_posted field in the Post model.
3. User is a built-in Django model for handling user authentication. 
It provides fields like username, email, and password, as well as methods for user 
authentication and management.
"""


# Create your models here.
# Define a Django model (database table) named 'Post'
class Post(models.Model):
    # Define a CharField named 'title' with a maximum length of 100 characters
    title = models.CharField(max_length=100)

    # Define a TextField named 'content' for storing longer text content
    content = models.TextField()

    # Define a DateTimeField named 'date_posted' with a default value of the current time
    date_posted = models.DateTimeField(default=timezone.now)

    # Define a ForeignKey named 'author' that creates a many-to-one relationship
    # with the User model from django.contrib.auth.models
    # on_delete=models.CASCADE specifies that if the associated User is deleted,
    # all related Post instances should be deleted as well (CASCADE deletion)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define a human-readable string representation of the Post instance
    def __str__(self):
        return self.title
```

2. Update the database to reflect the changes made in the `blog/models.py`
```bash
# Create database migration files based on changes in the models
py manage.py makemigrations
# Apply pending database migrations to update the database schema
py manage.py migrate
```
- Note: Commands above will create a new migration file (e.g. `blog/migrations/0001_initial.py`)

```bash
# To see the actual SQL commands that migration will run, try:
py manage.py sqlmigrate blog 0001

# Output: 
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

3. Django Database Operations Demo:
```bash
# Enter Djago Shell
py manage.py shell
```

```python
from blog.models import Post
from django.contrib.auth.models import User
User.objects.all()
# Output: <QuerySet [<User: ii777>]>
User.objects.first()
# Output: <User: ii777>
User.objects.filter(username='ii777')
# Output: <QuerySet [<User: ii777>]>
User.objects.filter(username='ii777').first()
# Output: <User: ii777>
user = User.objects.filter(username='ii777').first()
user
# Output: <User: ii777>
user.id
# Output: 1
user.pk
# Output: 1
user = User.objects.get(id=1)
user
# Output: <User: ii777>
Post.objects.all() 
# Output: <QuerySet []>
post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
Post.objects.all() 
# Output: <QuerySet []>
post_1.save()
Post.objects.all() 
# Output: <QuerySet [<Post: Blog 1>]>
# if __str__ method is not defined in models.py:
# Output: <QuerySet [<Post: Post object (1)>]> 
post_2 = Post(title='Blog 2', content='Second Post Content!', author_id=user.id)
post_2.save()
post_3 = Post(title='Blog 3', content='First Post Content!', author_id=user.id)
post_3.save()
post = Post.objects.first()
post.content
# Output: 'First Post Content!'
post.date_posted
# Output: datetime.datetime(2023, 12, 27, 23, 7, 12, 72939, tzinfo=<UTC>)
post.author
# Output: <User: ii777>
post.author.email
# Output: 'test@test.com'
user
# Output: <User: ii777>
user.post_set
# Output: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x7cd89f648fa0>
user.post_set.all()
<QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>
user.post_set.create(title='Blog 4', content='Fourth Post Content!')
# Output: <Post: Blog 4>
user.post_set.all()
# Output: <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>, <Post: Blog 4>]>
exit()
```

4. Update `blog/views.py` to use data from the database instead of hardcoded blog posts
```python
# blog/views.py
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
```

5. Update `blog/templates/blog/home.html`
```html
{% extends "blog/base.html" %}
{% block content %}
{% for post in posts %}
<article class="media content-section">
  <div class="media-body">
    <div class="article-metadata">
      <a class="mr-2" href="#">{{ post.author }}</a>
      <small class="text-muted">{{ post.date_posted|date:"Y-m-d H:i" }}</small>
    </div>
    <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
    <p class="article-content">{{ post.content }}</p>
  </div>
</article>
{% endfor %}
{% endblock content %}
```

6. Update `blog/admin.py` to register the new model
```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```

## Part 6 - User Registration
1. Create users app
```bash
py manage.py startapp users
```

### The `startapp` command cretes the following file structure:
- new file:   users/__init__.py
- new file:   users/admin.py
- new file:   users/apps.py
- new file:   users/migrations/__init__.py
- new file:   users/models.py
- new file:   users/tests.py
- new file:   users/views.py

### Changes made:
- new file:   users/templates/users/register.html
- modified:   blog/templates/blog/base.html
- modified:   django_project/settings.py
- modified:   django_project/urls.py
- modified file:   users/forms.py
- modified file:   users/views.py

2. Register the new app `users` + `crispy_forms` in the `django_project/settings.py` 
```python
# django_project/settings.py 
INSTALLED_APPS = [
    'blog',
    'users',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

3. Edit project-level routes in `django_project/urls.py`
```python
# django_project/urls.py
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
```

4. Edit `users/views.py` to handle user registration, form validation, redirects and messages. 
```python
# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


# Define a view function for user registration
def register(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create an instance of the UserRegisterForm with the POST data
        form = UserRegisterForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to create a new user
            form.save()

            # Get the username from the cleaned data of the form
            username = form.cleaned_data.get('username')

            # Display a success message using Django messages framework
            messages.success(request, f'Account created for {username}!')

            # Redirect the user to the home page
            return redirect('blog-home')
    else:
        # If the request method is not POST, create an empty UserRegisterForm instance
        form = UserRegisterForm()

    # Render the register.html template with the form in the context
    return render(request, 'users/register.html', {'form': form})
```

5. Create `users/forms.py`
```python
# users/forms.py
# This module provides functionalities to build web forms.
from django import forms
# This model represents a user in the database.
from django.contrib.auth.models import User
# This class takes care of creating user registration forms with password handling.
from django.contrib.auth.forms import UserCreationForm


# Define a custom user registration form, inheriting from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Add an optional email field to the form
    email = forms.EmailField(required=False)  # makes email field optional
    # email = forms.EmailField() # Uncomment to make the email field required

    class Meta:
        # Specify the model to use (User) and the fields to include in the form
        model = User
        fields = ["username", "email", "password1", "password2"]
```

6. Add a `users/templates/users/register.html` template
```html
<!-- users/templates/users/register.html -->
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
<!-- Extends the base.html template for consistent styling -->
<div class="content-section">
    <!-- Main content section -->
    <form method="POST">
        <!-- Form for user registration using the POST method -->
        {% csrf_token %}
        <!-- Include a CSRF token for security -->
        <fieldset class="form-group">
            <!-- Fieldset to group form elements with a legend -->
            <legend class="border-bottom mb-4">Join Today</legend>
            <!-- Legend for the form section -->
            {{ form|crispy }}
            <!-- Render the form using the crispy_forms_tags to apply styling -->
        </fieldset>
        <div class="form-group">
            <!-- Additional form group for the submit button -->
            <button class="btn btn-outline-info" type="submit">Sign Up</button>
            <!-- Submit button for the form -->
        </div>
    </form>
    <div class="border-top pt-3">
        <!-- Additional content section with border and padding at the top -->
        <small class="text-muted">
            <!-- Small text with muted color -->
            Already Have An Account? <a class="ml-2" href="#">Sign In</a>
            <!-- Display a link for users who already have an account -->
        </small>
    </div>
</div>
{% endblock content %}
```

## Part 7 - Login and Logout System

## Part 8 - User Profile and Picture

## Part 9 - Update User Profile

## Part 10 - Create, Update, and Delete Posts

## Part 11 - Pagination

## Part 12 - Email and Password Reset
