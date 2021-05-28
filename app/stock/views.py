from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.forms import LoginForm, MessageForm
from stock.models import ChatRoomMessages

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
# def logged(request):
#     return render(request, "stock/authenticated.html", context={})
# def logout_view(request):
#     logout(request)
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
        msg_objs = ChatRoomMessages.objects.filter().order_by("-sended_datetime")[:50:-1]

        quotes = []
        for msg_obj in msg_objs:
            quotes.append(
                {
                    "datetime":str(msg_obj.sended_datetime),# this date should be prettier in a pattern
                    "name": msg_obj.user_name,
                    "message": msg_obj.message
                }
            )

        message_form = MessageForm()

        html_data = {
            "quotes": quotes,
            "message_form": message_form
            }
        return render(request, "stock/chat_page.html", context=html_data)

    def post(self, request):
        message_form = MessageForm(request.POST)
        if not message_form.is_valid():
            return redirect("stock:login")

        if not request.user:
            return redirect("stock:login")

        message = message_form.cleaned_data["message"]

        # create a new quote message
        user_name = request.user.username
        quote = ChatRoomMessages(
            user_name = user_name,
            message = message
            )
        quote.save()

        return redirect("stock:logged")


class ChatDataView(LoginRequiredMixin, View):

    def get(self, request):
        msg_obj = ChatRoomMessages.objects.filter().order_by("sended_datetime")[:50]
        chat_room_messages = ChatRoomMessages()
