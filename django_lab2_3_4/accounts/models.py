from django.db import models

class Acc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
