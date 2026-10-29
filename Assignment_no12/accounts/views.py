import re
from django.shortcuts import render

def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        username_pattern = r"^[A-Za-z0-9_]{3,20}$"
        password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"

        if not re.fullmatch(username_pattern, username):
            message = "Invalid username!"

        elif not re.fullmatch(password_pattern, password):
            message = "Invalid password!"

        else:
            message = "Login successful!"

    return render(request, "login.html", {"message": message})