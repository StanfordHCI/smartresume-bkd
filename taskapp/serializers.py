from rest_framework import serializers
from models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = '__all__'


class GuildWorkerMapSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer()
    guild = GuildSerializer()
    class Meta:
        model = GuildWorkerMap
        fields = ('created', 'last_modified', 'worker', 'guild')