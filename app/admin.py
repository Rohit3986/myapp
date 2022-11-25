from django.contrib import admin
from .models import ToDo,Tags
# Register your models here.

@admin.register(ToDo)
class TodoAdmin(admin.ModelAdmin):
    list_display=["id","title","description","due_date","status","timestamp"]

@admin.register(Tags)
class TodoAdmin(admin.ModelAdmin):
    list_display=["id","tag_name"]