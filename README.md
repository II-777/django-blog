# Django Blog

## Part 1 - Getting Started
```bash
# create and start python3 virtual environment 
py -m venv .venv
source .venv/bin/activate
# install required python3 modules 
pip install -r requirements.txt
# create a django project
django-admin startproject django_project
```

### The `startproject` command cretes the following django file structure:
- new file:   django_project/__init__.py
- new file:   django_project/settings.py
- new file:   django_project/urls.py
- new file:   django_project/wsgi.py
- new file:   manage.py
- new file:   db.sqlite3

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
```bash
# create a django app
py manage.py startapp blog
```
### The `startapp` command cretes the following django file structure: - new file:   blog/__init__.py
- new file:   blog/admin.py
- new file:   blog/apps.py
- new file:   blog/migrations/__init__.py
- new file:   blog/models.py
- new file:   blog/tests.py

1. Modify `django_project/settings.py` to register the new app
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

2. Create views for `home page` and `about page`
```python
# blog/views.py
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
```

3. Create **app-level routes** for `home page`, `blog page` and `about page`
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

4. Create **project-level routes** for `home page`, `blog page` and `about page`
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
from django.shortcuts import render

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


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
```

## Part 4 - Admin Page
```bash
# create a superuser account
py manage.py makemigrations
py manage.py migrate
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

### Changes committed:
- modified:   blog/views.py
- modified:   blog/models.py
- new file:   blog/migrations/0001_initial.py
- modified:   blog/templates/blog/home.html
- modified:   blog/admin.py

1. Modify `blog/models.py` file to display database data
```python
# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

2. Update the database to reflect the changes made in the `blog/models.py`
```bash
# updaet the database
py manage.py makemigrations
py manage.py migrate
```
- Note: Commands above will create a new migration file (e.g. `blog/migrations/0001_initial.py`)

### To see the actual SQL commands that migration will run, try:
```bash
py manage.py sqlmigrate blog 0001
```
```bash
# Output: 
BEGIN;
--
-- Create model Post
--
CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL, "date_posted" datetime NOT NULL, "author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
COMMIT;
```

1. Django Database Operations Demo:
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

3. Update blog/views.py to use data from the database instead of hardcoded blog posts
```python
from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
```

4. Update `blog/templates/blog/home.html`
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

5. Update `blog/admin.py` to register the new model
```python
from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
```
## Part 6 - User Registration

## Part 7 - Login and Logout System

## Part 8 - User Profile and Picture

## Part 9 - Update User Profile

## Part 10 - Create, Update, and Delete Posts

## Part 11 - Pagination

## Part 12 - Email and Password Reset
