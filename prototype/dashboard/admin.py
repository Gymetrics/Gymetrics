from django.contrib import admin
from .models import Stream
# Register your models here.


class StreamAdmin(admin.ModelAdmin):
    list_display = ['name', 'status','live']


admin.site.register(Stream, StreamAdmin)