from django.db import models


# Create your models here.
class SqlModel(models.Model):
    sql_name = models.CharField(max_length=200)
