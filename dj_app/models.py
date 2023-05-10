from typing import Any
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    friend_list = models.ManyToManyField('User', blank=True)
    request_list = models.ManyToManyField('Request', blank=True)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender_user')
    recepient = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='recipient_user')