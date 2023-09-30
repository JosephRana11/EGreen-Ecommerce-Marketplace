from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
  msg = models.TextField()
  sender = models.ForeignKey(User , on_delete=models.CASCADE)
  sent_at = models.DateTimeField(auto_now_add=True)