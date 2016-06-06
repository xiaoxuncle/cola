from django.contrib.auth.models import User
from django.db import models

class CommonUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(default='avatar/default_avatar.png')
    mysite = models.CharField(max_length=255, null=True)
    career = models.CharField(max_length=255, null=True)
    introduction = models.TextField(max_length=3000, null=True)

    class Meta:
        verbose_name = 'Common user'
        verbose_name_plural = 'Common users'

    def __str__(self):
        return self.user.username
