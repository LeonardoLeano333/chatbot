from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.forms import LoginForm

# TODO: create the chat room
# - create a view that shows the 50 messages from the model model timestamp, username and messages 
# - create a template with a char field to be posted
# - in the post get the user data and write in model timestamp, username and messages

# TODO: create a chat bot using a celery as a cron 1min with rabitmq
# bot:
# - get data from "https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv"
# - parse the csv with ","
# - send it for the model(timestamp, username and messages) with the messages time to time(1min)

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