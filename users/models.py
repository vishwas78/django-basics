from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="User")
    password = models.CharField(max_length=20, verbose_name="Password")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


