from django.contrib import admin
from models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_modified', 'worker_name', 'worker_id', 'requester_name', 'requester_id', 'hit_id', 'title', 'reward', 'status', 'feedback')

admin.site.register(Task, TaskAdmin)