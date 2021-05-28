from django.db import models

# Create your models here.
class ChatRoomMessages(models.Model):
    sended_datetime = models.DateTimeField(auto_now_add=True)
    chat_room_name = models.CharField(max_length=30, default="base")
    user_name = models.CharField(max_length=30) # use this field as a relation ship with the admin base model
    message = models.CharField(max_length=280) # same as Twitter
