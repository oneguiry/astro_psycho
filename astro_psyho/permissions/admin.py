from django.contrib import admin

from permissions.models import AccountManager


@admin.register(AccountManager)
class AccountManagerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name',]