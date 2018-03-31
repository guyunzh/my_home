from django.db import models
from django.contrib.auth.models import User


class UserInfo(User):
    telephone = models.CharField(max_length=20, blank=True)
    qq = models.CharField(max_length=20, blank=True)
    birth = models.DateTimeField(null=True)
    company = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return 'user:{}' .format(self.username)


