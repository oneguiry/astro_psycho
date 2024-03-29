from django.contrib import admin

from core.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title', 'author', 'pub_date')
    list_filter = ('title', 'author', 'pub_date')
