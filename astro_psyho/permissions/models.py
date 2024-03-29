from django.contrib.auth.models import User
from django.db import models


class AccountManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False, blank=False)
    date_of_birth = models.DateField(null=False, auto_created=False)
