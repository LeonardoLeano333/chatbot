from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.forms import LoginForm

# implement this others latter
# TODO: START implement this later
def logged(request):
    return render(request, "stock/authenticated.html", context={})
def logout_view(request):
    logout(request)
    # Redirect to a success page.
# TODO: END implement this latter

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        html_data = {"login_form":login_form}
        return render(request, "stock/login.html", context=html_data)

    def post(self, request):
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

class ChatView(LoginRequiredMixin, View):
    login_url = "/"
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, "stock/authenticated.html", context={})