from django.db import models
from django.utils import timezone

# Create your models here.


class Quize(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)
