from django.contrib import admin
from models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_modified', 'name', 'is_checked', 'due_date', 'notes')

admin.site.register(Task, TaskAdmin)