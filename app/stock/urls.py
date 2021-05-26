  
from django.urls import path
from stock import views

app_name = 'stock'

urlpatterns = [
    path("", views.login_view, name='login'),
    path("login", views.login_post, name='login_post'), 
    path("logged", views.logged, name='logged'),
    ]