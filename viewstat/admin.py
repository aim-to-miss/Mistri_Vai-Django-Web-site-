from django.contrib import admin

# Register your models here.
from .models import homestat,comments,mistri

admin.site.register(homestat)
admin.site.register(comments)
admin.site.register(mistri)