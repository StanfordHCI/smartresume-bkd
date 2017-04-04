from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend

# Create your views here.
from models import *
from serializers import *

class TaskViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: Task is the model for the "tasks".
    * CRUD on Task model
    * C - CREATE - POST /task/ - allowed for anyone
    * R - READ - GET /task/ (list) - allowed for anyone
    * R - READ - GET /task/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /task/[id]/ - allowed for anyone
    * D - DELETE - DELETE /task/[id]/ - allowed for anyone
    '''
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)  
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = TaskSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: Worker is the model for the "workers".
    * CRUD on Worker model
    * C - CREATE - POST /worker/ - allowed for anyone
    * R - READ - GET /worker/ (list) - allowed for anyone
    * R - READ - GET /worker/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /worker/[id]/ - allowed for anyone
    * D - DELETE - DELETE /worker/[id]/ - allowed for anyone
    '''
    queryset = Worker.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)  
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = WorkerSerializer

class GuildViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: Guild is the model for the "guilds".
    * CRUD on Guild model
    * C - CREATE - POST /guild/ - allowed for anyone
    * R - READ - GET /guild/ (list) - allowed for anyone
    * R - READ - GET /guild/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /guild/[id]/ - allowed for anyone
    * D - DELETE - DELETE /guild/[id]/ - allowed for anyone
    '''
    queryset = Guild.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)  
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = GuildSerializer

class GuildWorkerMapViewSet(viewsets.ModelViewSet):
    '''
    * Model Description: GuildWorkerMap is the model for the "guildworkermap".
    * CRUD on GuildWorkerMap model
    * C - CREATE - POST /guildworkermap/ - allowed for anyone
    * R - READ - GET /guildworkermap/ (list) - allowed for anyone
    * R - READ - GET /guildworkermap/[id]/ (detail) - allowed for anyone
    * U - UPDATE - PATCH /guildworkermap/[id]/ - allowed for anyone
    * D - DELETE - DELETE /guildworkermap/[id]/ - allowed for anyone
    '''
    queryset = GuildWorkerMap.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)  
    permission_classes = (AllowAny,)
    filter_fields = '__all__'
    serializer_class = GuildWorkerMapSerializer

