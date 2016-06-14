from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	user = models.ForeignKey(User)
	message = models.TextField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
