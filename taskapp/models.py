from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Task(models.Model):
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    name = models.TextField(default='', blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    notes = models.TextField(default='', blank=True, null=True)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text
