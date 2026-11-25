from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":
        firstName = request.POST.get("firstname", "").strip().title()
        lastName = request.POST.get("lastname", "").strip().title()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("confirm_password", "")
        # terms = request.POST.get("terms", "")

        if firstName == None or lastName == None or email == None or username == None or password == None:
            messages.info(request, "All fields are required!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken!")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email is already taken!")
            return redirect("signup")

        if password != password2:
            messages.info(request, "Passwords do not match!")
            return redirect("signup")

        if len(password) < 8:
            messages.info(request, "Password must be at least 8 characters")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            first_name=firstName,
            last_name=lastName,
            email=email,
            password=password2,
            # terms=terms,
        )
        user.save()
        print(f"User {user.first_name} {user.last_name} with username {user.username} and email {user.email} and password {user.password} was created")
        return redirect("signin")
        
    else:
        return render(request, "signup.html")