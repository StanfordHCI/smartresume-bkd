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

class Worker(models.Model): 
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    worker_name = models.TextField(default='', blank=True, null=True)
    worker_id = models.TextField(default='', blank=True, null=True)

    def __unicode__(self):
        return self.worker_name

    def __str__(self):
        return self.worker_name

class Guild(models.Model): 
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    guild_name = models.TextField(default='', blank=True, null=True)
    guild_creator_id = models.TextField(default='', blank=True, null=True) 
    guild_creator_type = models.BooleanField(default=False) # false for requestor, true for worker (also false for requestor that is also a worker, i.e. like the "Govinda Dasu" in worker/requester sandbox)

    def __unicode__(self):
        return self.guild_name

    def __str__(self):
        return self.guild_name

class GuildWorkerMap(models.Model):
    created = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow, blank=True, null=True)     
    worker = models.ForeignKey('Worker', blank=True, null=True, related_name='guildworkermap_worker')
    guild = models.ForeignKey('Guild', blank=True, null=True, related_name='guildworkermap_guild')

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text
