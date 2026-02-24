from django.shortcuts import render, redirect
from .models import Ragister, Contact, CustomUser, LoginAttempt  #  Change model names here if renamed
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password  #  For password hashing
from .forms import CustomUserForm
from .forms import LoginForm  #  make sure this is imported
from .forms import ContactForm  # Import your ContactForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import render, redirect

# Static page — no form
def index(request):
    return render(request,'index.html')

# Static page — no form
def about(request):
    return render(request,'about.html')

# Static page — no form
def blog(request):
    return render(request,'blog.html')

# Static page — no form
def course_inner(request):
    return render(request,'course_inner.html')

# Static page — no form
def course(request):
    return render(request,'course.html')

# Static page — no form
def post(request):
    return render(request,'post.html')

# Base layout
def base(request):
    return render(request,'base.html')

# Static page — no form
def learnmore_home(request):
    return render(request,'learnmore_home.html')

#  Success page — used after any form submission
def success(request):
    return render(request, 'success.html')  #  Must create success.html

#  Contact Page (Form 2 handling)# views.py
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('contact')  # Redirect to success page after saving
    else:
        form = ContactForm()  # Initialize empty form for GET request
    return render(request, 'contact.html', {'form': form})  # Pass form to template


#  Home Page (Form 1 handling)
def home(request):
    if request.method == "POST":
        #  Save lead data to DB
        Ragister.objects.create(  #  Rename model if needed
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number")
        )
        return redirect('home')  #  Redirect after success
    return render(request,'home.html')  #  Must match template file


#  Login Form (Form 4)

# views.py
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_course')  # or your desired view
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})  # 🟢 form pass hona chahiye

#  Signup Form (Form 3)

def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)  #  Use the custom form with validations
        if form.is_valid():
            user = form.save(commit=False)  #  Don't save yet, we need to hash password
            user.password = make_password(form.cleaned_data["password1"])  #  Secure password
            user.save()  #  Save to DB
            return redirect('login')  #  Change this to your success URL/view
        else:
            return render(request, 'signup.html', {'form': form})  #  Show form errors
    else:
        form = CustomUserForm()  #  Empty form for GET request
    return render(request, 'signup.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Handle the subscription (save the email, send confirmation, etc.)
            email = form.cleaned_data['email']
            # Do something with the email, e.g., save it to the database or send a confirmation email.
            return render(request, 'login.html')  # Redirect to success page or show success message
    else:
        form = SubscriptionForm()
    
    return render(request, 'subscribe.html', {'form': form})



def my_course(request):
    return render(request, 'my_course.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # or any other page you want to redirect to after updating
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Assuming 'login' is the name of a URL pattern
