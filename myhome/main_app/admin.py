from django.contrib import admin
from .models import MessageModel


class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'telephone', 'qq']
    search_fields = ['name', 'telephone']


admin.site.register(MessageModel,MessageModelAdmin)
