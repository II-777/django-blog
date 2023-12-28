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
