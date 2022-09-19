from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_profile', 'rick_name')
    search_fields = ('url_profile',)
    empty_value_display = '-пусто-'
