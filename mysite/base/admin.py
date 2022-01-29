from django.contrib import admin

# Register your models here.

from .models import POST, Topic

admin.site.register(POST)
admin.site.register(Topic)