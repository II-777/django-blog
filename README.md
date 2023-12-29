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
# Changes Made:
1. modified:   django_project/urls.py
2. modified:   blog/templates/blog/base.html
3. modified:   django_project/settings.py
4. new file:   users/templates/users/login.html
5. new file:   users/templates/users/logout.html
6. new file:   users/templates/users/profile.html
7. modified:   users/templates/users/register.html
8. modified:   users/views.py
  
1. Edit project-level `django_project/urls.py` to add routes to `login`, `logout` and `profile` pages
```python
# django_project/urls.py
# Import the admin module for Django's administration site
from django.contrib import admin
# Import functions for defining URL patterns
from django.urls import path, include
# Import the 'register' view from the 'users' app's views module and alias it as 'user_views'
from users import views as user_views
# Import views from Django's authentication module for handling authentication-related views
from django.contrib.auth import views as auth_views

# Define URL patterns for the Django project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # Include URL patterns from the 'blog' app
    path('', include('blog.urls')),
    # User registration URL, mapped to the 'register' view
    path('register/', user_views.register, name='register'),
    # Profile view for the 'profile/' URL
    path('profile/', user_views.profile, name='profile'),
    # Login view using Django's built-in LoginView with a custom template
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout view using Django's built-in LogoutView with a custom template
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Include additional URL patterns from the 'blog.urls' module
    path('', include('blog.urls')),
]
```

2. Edit `blog/templates/blog/base.html` to add right side navigation url blocks
```html
          <!-- Navbar Right Side with Login and Register links -->
          <div class="navbar-nav">
            {% if user.is_authenticated %}
            <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
            <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
            {% else %}
            <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
            <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
            {% endif %}
          </div>
```

3. Edit `django_project/settings.py`
```python
# django_project/settings.py
# Specifies the template pack for django-crispy-forms.
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Redirects unauthenticated users to the login page.
LOGIN_URL = 'login'
# Redirects users after a successful login.
LOGIN_REDIRECT_URL = 'blog-home'
```

4. Add `users/templates/users/login.html`
```html
<!-- users/templates/users/login.html -->
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Log In</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Login</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Don't have an Account? <a class="ml-2" href="{% url 'register' %}">Sign Up Now</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

5. Add `users/templates/users/logout.html`
```html
<!-- users/templates/users/logout.html -->
{% extends "blog/base.html" %}
{% block content %}
<h2>You have logged out</h2>
<div class="border-top pt-3">
    <small class="text-muted">
        <a href="{% url 'login' %}">Log in again</a>
    </small>
</div>
{% endblock content %}
```

6. Add `users/templates/users/profile.html`
```html
<!-- users/templates/users/profile.html -->
{% extends "blog/base.html" %}
{% block content %}
    <h1>{{ user.username }}</h1>
{% endblock content %}
```

7. Edit `users/templates/users/register.html` to add login url block
```html
<!-- users/templates/users/register.html -->
Already Have An Account? <a class="ml-2" href="{% url 'login' %}">Sign In</a>
```

8. Edit `users/views.py` to add login restricted `profile` page
```python
# users/views.py 
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# Define a view function for user registration
def register(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Create an instance of the UserRegisterForm with the POST data
        form = UserRegisterForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data to create a new user
            form.save()

            # Get the username from the cleaned data of the form
            username = form.cleaned_data.get("username")

            # Display a success message using Django messages framework
            messages.success(request, f"Account created for {username}!")

            # Redirect the user to the home page
            return redirect("blog-home")
    else:
        # If the request method is not POST, create an empty UserRegisterForm instance
        form = UserRegisterForm()

    # Render the register.html template with the form in the context
    return render(request, "users/register.html", {"form": form})

# Decorator to require login for the profile view
@login_required
def profile(request):
    return render(request, "users/profile.html")

# The following comments explain the message levels available in the messages framework
# message.debug: Low-level debug information
# message.info: General information or status update
# message.success: Indicate a successful or positive action
# message.warning: Indicate a warning or potential problem
# message.error: Indicate an error or critical issue
```


## Part 8 - User Profile and Picture
### Changes made:
1. Edit `users/models.py`
```python
# users/models.py
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Define a Django model called 'Profile' that inherits from the 'Model' class
class Profile(models.Model):
    # Create a one-to-one relationship with the built-in User model in Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Define an image field for the profile picture, with a default image and upload directory
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Define a string representation for the Profile model, returning the username and 'Profile'
    def __str__(self):
        return f'{self.user.username} Profile'
```

2. Run 
```bash
# Install Pillow module
pip install Pillow
# Create database migration files based on changes in the models
py manage.py makemigrations
# Apply pending database migrations to update the database schema
py manage.py migrate
```

3. Edit `users/admin.py` to register the `Profile` model
```python
# users/admin.py
from django.contrib import admin
from .models import Profile

# Register your models here.
admin.site.register(Profile)
```

4. Add profiles for ii777 (with avatar) and user1 (no avatar) via admin interface
5. Activate Django shell
```bash
py manage.py shell
```
6. Run  
```python
from django.contrib.auth.models import User
user = User.objects.filter(username='ii777').first()
user
# Output: <User: ii777>
user.profile
# Output: <Profile: ii777 Profile>
user.profile.image
# Output: <ImageFieldFile: profile_pics/avatar.jpeg>
user.profile.image.width
# Output: 460
user.profile.image.height
# Output: 460
user.profile.image.url
# Output: 'profile_pics/avatar.jpeg'
user = User.objects.filter(username='user1').first()
user
# Output: <User: user1>
user.profile.image
# Output: <ImageFieldFile: default.jpg>
user.profile.image.url
# Output: 'default.jpg'
``` 

7. Edit `django_project/settings.py` to add the following:
```python
# django_project/settings.py
# Define the absolute filesystem path to the directory that will hold user-uploaded media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Define the base URL that will be used to serve media files uploaded by users.
MEDIA_URL = '/media/'

# Set the default auto-generated field for primary keys to BigAutoField
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### Note:
```python
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

This setting ensures that Django will use the `BigAutoField` as the default auto-generated field for primary keys in models. The `BigAutoField` is a 64-bit integer-based primary key, and by setting `DEFAULT_AUTO_FIELD` in this way, you're instructing Django to use this type of field unless a different primary key field is explicitly specified for a particular model.


8. Edit `users/apps.py`
```python
# users/apps.py
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        import users.signals
```

9. Edit `users/urls.py` to add the following:
```python
# users/urls.py
# Import necessary modules from Django
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views  # Import views from the 'users' app

# Define the URL patterns for the application
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    # User registration URL
    path('register/', user_views.register, name='register'),
    # User profile URL
    path('profile/', user_views.profile, name='profile'),
    # Login URL
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # Include URLs from the 'blog' app
    path('', include('blog.urls')),
]

# If the application is in DEBUG mode, add URL patterns for serving media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

9. Add the `users/templates/users/profile.html` template
```python
# users/templates/users/profile.html
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
      <div class="media">
        <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
        <div class="media-body">
          <h2 class="account-heading">{{ user.username }}</h2>
          <p class="text-secondary">{{ user.email }}</p>
        </div>
      </div>
      <!-- FORM HERE -->
    </div>
{% endblock content %}
```

10. Add the default avatar file `media/default.jpg`

## Part 9 - Update User Profile
# Changes made:
- modified:   blog/templates/blog/home.html
- modified:   users/forms.py
- modified:   users/models.py
- modified:   users/templates/users/profile.html
- modified:   users/views.py

1. Edit `users/forms.py`
```python
# users/forms.py
# Import necessary modules and classes from Django
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Import Profile model from the current app
from .models import Profile

# Form for user registration, extending Django's built-in UserCreationForm
class UserRegisterForm(UserCreationForm):
    # Additional email field for registration form
    email = forms.EmailField()

    class Meta:
        # Specify the model and fields for the form
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for updating user information, extending Django's ModelForm
class UserUpdateForm(forms.ModelForm):
    # Additional email field for user update form
    email = forms.EmailField()

    class Meta:
        # Specify the model and fields for the form
        model = User
        fields = ['username', 'email']

# Form for updating user profile information, extending Django's ModelForm
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # Specify the model and fields for the form
        model = Profile
        fields = ['image']
```

2. Edit `users/models.py`
```python
# users/models.py
# Import necessary modules and classes from Django
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Model for user profiles, extending Django's Model class
class Profile(models.Model):
    # One-to-One relationship with the built-in User model, deleting profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # ImageField for user profile pictures, with default and upload path
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        # String representation of the profile, displaying the associated username
        return f'{self.user.username} Profile'

    def save(self):
        # Call the save method of the parent class (Model) before additional operations
        super().save()

        # Open the image associated with the profile
        img = Image.open(self.image.path)

        # Resize the image if it exceeds a certain size
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

3. Edit `users/views.py`
```python
# users/views.py
# Import necessary modules and classes from Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Import user-related forms from the current app
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# View function for user registration
def register(request):
    # Handle form submission
    if request.method == 'POST':
        # Create a registration form with the submitted data
        form = UserRegisterForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data and create a new user
            form.save()
            username = form.cleaned_data.get('username')
            # Display a success message and redirect to the login page
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        # If it's a GET request, create an empty registration form
        form = UserRegisterForm()

    # Render the registration page with the form
    return render(request, 'users/register.html', {'form': form})

# View function for user profile
@login_required
def profile(request):
    # Handle form submission
    if request.method == 'POST':
        # Create user update form and profile update form with the submitted data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # Check if both forms are valid
        if u_form.is_valid() and p_form.is_valid():
            # Save the updated user and profile information
            u_form.save()
            p_form.save()
            # Display a success message and redirect to the profile page
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        # If it's a GET request, create user update form and profile update form with the current user data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Create a context with user update form and profile update form
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    # Render the profile page with the user update form and profile update form
    return render(request, 'users/profile.html', context)
```

4. Edit `users/templates/users/profile.html`
```html
<!-- users/templates/users/profile.html -->
{% extends "blog/base.html" %}

{% load crispy_forms_tags %}

{% block content %}
    <!-- Start of content-section -->
    <div class="content-section">
        <!-- User profile display section -->
        <div class="media">
            <!-- Display user profile image -->
            <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
            <div class="media-body">
                <!-- Display username as a heading -->
                <h2 class="account-heading">{{ user.username }}</h2>
                <!-- Display user email as secondary text -->
                <p class="text-secondary">{{ user.email }}</p>
            </div>
        </div>

        <!-- Form for updating user profile information -->
        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <!-- Fieldset for organizing form fields with a legend -->
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Profile Info</legend>
                <!-- Render user update form and profile update form using crispy forms -->
                {{ u_form|crispy }}
                {{ p_form|crispy }}
            </fieldset>

            <!-- Form submission button -->
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Update</button>
            </div>
        </form>
    </div>
    <!-- End of content-section -->
{% endblock content %}
```

5. Edit `blog/templates/blog/home.html`
```html
<!-- blog/templates/blog/home.html -->
{% extends "blog/base.html" %}

{% block content %}
    <!-- Iterate over each post in the 'posts' queryset -->
    {% for post in posts %}
        <!-- Start of article container with media class for styling -->
        <article class="media content-section">
            <!-- Display the profile image of the post author -->
            <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
            <div class="media-body">
                <!-- Display post metadata (author and date) in a separate div -->
                <div class="article-metadata">
                    <!-- Display a link to the author's profile page -->
                    <a class="mr-2" href="#">{{ post.author }}</a>
                    <!-- Display the date when the post was created -->
                    <small class="text-muted">{{ post.date_posted|date:"Y-m-d H:i" }}</small>
                </div>
                <!-- Display post title as a heading -->
                <h2><a class="article-title" href="#">{{ post.title }}</a></h2>
                <!-- Display post content -->
                <p class="article-content">{{ post.content }}</p>
            </div>
        </article>
        <!-- End of article container -->
    {% endfor %}
{% endblock content %}
```

## Part 10 - Create, Update, and Delete Posts

### Changes made:
- modified:   blog/models.py
- modified:   blog/urls.py
- modified:   blog/views.py
- modified:   blog/templates/blog/base.html
- modified:   blog/templates/blog/home.html
- new file:   blog/templates/blog/post_confirm_delete.html
- new file:   blog/templates/blog/post_detail.html
- new file:   blog/templates/blog/post_form.html

1. Edit `blog/models.py`
```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
```

2. Edit **app-level routes** in `blog/urls.py` for `home page`, `blog page` and `about page`
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

3. Edit `blog/views.py` 
```python
# blog/views.py
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

4. Edit `blog/templates/blog/base.html`
```html
<!-- blog/templates/blog/base.html -->
{% load static %}
<!DOCTYPE html>
<html>
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">

    {% if title %}
        <title>Django Blog - {{ title }}</title>
    {% else %}
        <title>Django Blog</title>
    {% endif %}
</head>
<body>
    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="{% url 'blog-home' %}">Django Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a>
              <a class="nav-item nav-link" href="{% url 'blog-about' %}">About</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              {% if user.is_authenticated %}
                <a class="nav-item nav-link" href="{% url 'post-create' %}">New Post</a>
                <a class="nav-item nav-link" href="{% url 'profile' %}">Profile</a>
                <a class="nav-item nav-link" href="{% url 'logout' %}">Logout</a>
              {% else %}
                <a class="nav-item nav-link" href="{% url 'login' %}">Login</a>
                <a class="nav-item nav-link" href="{% url 'register' %}">Register</a>
              {% endif %}
            </div>
          </div>
        </div>
      </nav>
    </header>
    <main role="main" class="container">
      <div class="row">
        <div class="col-md-8">
          {% if messages %}
            {% for message in messages %}
              <div class="alert alert-{{ message.tags }}">
                {{ message }}
              </div>
            {% endfor %}
          {% endif %}
          {% block content %}{% endblock %}
        </div>
        <div class="col-md-4">
          <div class="content-section">
            <h3>Our Sidebar</h3>
            <p class='text-muted'>You can put any information here you'd like.
              <ul class="list-group">
                <li class="list-group-item list-group-item-light">Latest Posts</li>
                <li class="list-group-item list-group-item-light">Announcements</li>
                <li class="list-group-item list-group-item-light">Calendars</li>
                <li class="list-group-item list-group-item-light">etc</li>
              </ul>
            </p>
          </div>
        </div>
      </div>
    </main>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
</body>
</html>
```
5. Edit `blog/templates/blog/home.html`
```html
<!-- blog/templates/blog/home.html -->
{% extends "blog/base.html" %}
{% block content %}
    {% for post in posts %}
        <article class="media content-section">
          <img class="rounded-circle article-img" src="{{ post.author.profile.image.url }}">
          <div class="media-body">
            <div class="article-metadata">
              <a class="mr-2" href="#">{{ post.author }}</a>
              <small class="text-muted">{{ post.date_posted|date:"Y-m-d H:i" }}</small> 
            </div>
            <h2><a class="article-title" href="{% url 'post-detail' post.id %}">{{ post.title }}</a></h2>
            <p class="article-content">{{ post.content }}</p>
          </div>
        </article>
    {% endfor %}
{% endblock content %}
```

6. Add `blog/templates/blog/post_confirm_delete.html`
```html
<!-- blog/templates/blog/post_confirm_delete.html -->
{% extends "blog/base.html" %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Delete Post</legend>
                <h2>Are you sure you want to delete the post "{{ object.title }}"</h2>
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-danger" type="submit">Yes, Delete</button>
                <a class="btn btn-outline-secondary" href="{% url 'post-detail' object.id %}">Cancel</a>
            </div>
        </form>
    </div>
{% endblock content %}
```

7. Add `blog/templates/blog/post_detail.html`
```html
<!-- blog/templates/blog/post_detail.html -->
{% extends "blog/base.html" %}
{% block content %}
  <article class="media content-section">
    <img class="rounded-circle article-img" src="{{ object.author.profile.image.url }}">
    <div class="media-body">
      <div class="article-metadata">
        <a class="mr-2" href="#">{{ object.author }}</a>
        <small class="text-muted">{{ object.date_posted|date:"F d, Y" }}</small>
        {% if object.author == user %}
          <div>
            <a class="btn btn-secondary btn-sm mt-1 mb-1" href="{% url 'post-update' object.id %}">Update</a>
            <a class="btn btn-danger btn-sm mt-1 mb-1" href="{% url 'post-delete' object.id %}">Delete</a>
          </div>
        {% endif %}
      </div>
      <h2 class="article-title">{{ object.title }}</h2>
      <p class="article-content">{{ object.content }}</p>
    </div>
  </article>
{% endblock content %}
```

8. Add `blog/templates/blog/post_form.html`
```html
<!-- blog/templates/blog/post_form.html -->
{% extends "blog/base.html" %}
{% load crispy_forms_tags %}
{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Blog Post</legend>
                {{ form|crispy }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Post</button>
            </div>
        </form>
    </div>
{% endblock content %}
```

## Part 11 - Pagination

## Part 12 - Email and Password Reset
