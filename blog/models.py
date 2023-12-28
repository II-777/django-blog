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
