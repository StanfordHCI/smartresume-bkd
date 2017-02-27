from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

# Create your views here.
from models import *
from serializers import *

class TaskViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: Task is the model for the "tasks" in the party planner app.
    * CRUD on Task model
    * C - CREATE - POST /task/ - allowed for anyone
    * R - READ - GET /task/ (list) - allowed for anyone
    * R - READ - GET /task/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /task/[id]/ - allowed for anyone
    * D - DELETE - DELETE /task/[id]/ - allowed for anyone
    '''
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = TaskSerializer