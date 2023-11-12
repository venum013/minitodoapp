from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now=True)
    