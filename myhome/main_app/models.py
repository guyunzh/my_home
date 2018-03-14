
from django.db import models


class MessageModel(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    qq = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.name
