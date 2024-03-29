from django.db import models

from permissions.models import AccountManager


class News(models.Model):
    title = models.CharField("Заголовок", max_length=40, unique=True, blank=False, null=False)
    body = models.TextField("Содержание поста")
    pub_date = models.DateField(auto_now=True)
    author = models.OneToOneField(AccountManager, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.user.email + self.title + self.pub_date
