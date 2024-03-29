from datetime import datetime

from django.contrib.auth.models import User

from permissions.models import AccountManager


class PermissionsController:
    def __init__(self, pk: int = None):
        self.acc = None
        if pk:
            self.account = AccountManager.objects.get(id=pk)

    def _create_super_user(self):
        try:
            user = User.objects.get(username="admin")
        except User.DoesNotExist:
            user = User.objects.create_user(username='admin', password='1', email='admin@mail.ru')
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()

            self.acc = AccountManager.objects.create(user=user, lastname="Elena", firstname="Elena",
                                                     date_of_birth=datetime.today())
            print(self.acc, "Пользователь админ создан")
        return self.acc
