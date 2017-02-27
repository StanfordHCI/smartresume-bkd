from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from taskapp.views import *

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]