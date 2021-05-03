from django.db import models
from django.utils import timezone

class Todo(models.Model) :
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    text = models.CharField(max_length=255, null=True, blank=True)
    done = models.BooleanField(null=True, blank=True)

