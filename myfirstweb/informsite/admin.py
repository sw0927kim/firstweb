from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('proposer', 'content')
    search_fields = ('proposer', 'content')

admin.site.register(Notice)
