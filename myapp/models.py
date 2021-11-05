from django.db import models
from django.db.models.aggregates import Max
import sys
from datetime import datetime
# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)