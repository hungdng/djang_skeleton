# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class TimestampedModel(models.Model):
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        ordering = ['-created_date', '-updated_date']
