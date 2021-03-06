from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class MessageForm(forms.Form):
    message = forms.CharField(max_length=280) # same as Twitter
