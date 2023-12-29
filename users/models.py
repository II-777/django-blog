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
