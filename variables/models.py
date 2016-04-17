from django.db import models

class Variable(models.Model):
    key = models.CharField(max_length=30)
    value = models.TextField()
    