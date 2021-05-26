  
from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path("", views.LoginView.as_view(), name='login'),
    path("logged", views.ChatView.as_view(), name='logged'),
    ]