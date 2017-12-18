from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
from .models import *
import bcrypt

  # the index function is called when root is visited
def index(request):
    if "id" not in request.session:
        request.session["id"] = 0
    return render(request, "first_app/index.html")

def register(request):
    errors = User.objects.regvalidator(request.POST)
    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/")
    else:
        new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()))
        request.session["id"] = new_user.id
        return redirect("/success")

def login(request):
    errors = User.objects.logvalidator(request.POST)

    if len(errors):
        for error in errors.itervalues():
            messages.error(request, error)
        return redirect("/")

    user_to_login = User.objects.get(email=request.POST["email"])
    if user_to_login == []:
        messages.error(request, "Invalid email or password.")
        return redirect("/")

    if bcrypt.checkpw(request.POST['pw'].encode(), user_to_login.password.encode()):
        request.session["id"] = user_to_login.id
        return redirect("/success")
    else:
        messages.error(request, "Invalid email or password.")
        return redirect("/")

def success(request):
    if request.session["valid"] == "Register":
        messages.success(request, "Successfully registered!")
    elif request.session["valid"] == "Login":
        messages.success(request, "Successfully logged in!")
    context = {
        "user": User.objects.get(id=request.session["id"])
    }
    return render(request, "first_app/success.html", context)
