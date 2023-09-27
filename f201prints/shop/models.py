from django.db import models

class PaperType(models.Model):
    name        = models.CharField(max_length=32, null=True, blank=True)
    dimension   = models.CharField(max_length=32, null=True, blank=True)
