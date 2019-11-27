from datetime import datetime

from django.db import models


# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False, null=False)
    created_by = models.CharField(max_length=80)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
