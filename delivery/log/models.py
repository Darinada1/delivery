from django.db import models


class login(models.Model):
    email = models.CharField('email', max_length=50)
    password = models.TextField('password')

    class Meta:
        verbose_name = 'password'
        verbose_name_plural = 'passwords'
