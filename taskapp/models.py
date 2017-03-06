from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Task(models.Model): # using hit_id+worker_id is the unique identifier
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    worker_name = models.TextField(default='', blank=True, null=True)
    worker_id = models.TextField(default='', blank=True, null=True)
    requester_name = models.TextField(default='', blank=True, null=True)
    requester_id = models.TextField(default='', blank=True, null=True)
    hit_id = models.TextField(default='', blank=True)
    title = models.TextField(default='', blank=True, null=True)
    reward = models.TextField(default='', blank=True, null=True)
    status = models.TextField(default='', blank=True, null=True)
    feedback = models.TextField(default='', blank=True, null=True)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text
