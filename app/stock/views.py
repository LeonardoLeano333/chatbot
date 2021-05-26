from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from stock.forms import LoginForm


def login_view(request):
    login_form = LoginForm()
    html_data = {"login_form":login_form}
    return render(request, "stock/login.html", context=html_data)


# this is a post
def login_post(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect("stock:logged")
    else:
        # Return an 'invalid login' error message.
        return redirect("stock:login")

def logged(request):
    return render(request, "stock/authenticated.html", context={})

def logout_view(request):
    logout(request)
    # Redirect to a success page.