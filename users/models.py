from django.db import models


class UsersData(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, default="Dj@eg.com")
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
