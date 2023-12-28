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


@login_required
def profile(request):
    return render(request, "users/profile.html")

# The following comments explain the message levels available in the messages framework
# message.debug: Low-level debug information
# message.info: General information or status update
# message.success: Indicate a successful or positive action
# message.warning: Indicate a warning or potential problem
# message.error: Indicate an error or critical issue