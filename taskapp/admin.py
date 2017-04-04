from django.contrib import admin
from models import *

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_modified', 'worker_name', 'worker_id', 'requester_name', 'requester_id', 'hit_id', 'title', 'reward', 'status', 'feedback')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('created', 'last_modified', 'worker_name', 'worker_id')

admin.site.register(Task, TaskAdmin)
admin.site.register(Worker, WorkerAdmin)

# admin does not matter for now, since no login yet, no authentication, so just can use the rest api