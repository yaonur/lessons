from django.db import models
from djongo import models as d_models


# Create your models here.
# class MongoModel(models.Model):
#     _id = d_models.ObjectIdField()
#     mongo_name = models.CharField(max_length=100, null=True, blank=True)
#     added_later = models.CharField('added_later_verbose_name', max_length=100, default='default_value', null=True,
#                                    blank=True)
#     added_later_2 = models.CharField('later_3', max_length=100, default='default_value', null=True, blank=True)
#
#     class Meta:
#         db_table = 'first_collection'
#
#     def __str__(self):
#         return self.mongo_name
#
#
# class MongoSecond(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         db_table = 'second_collection'


class Account(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=199)
    proxy = models.ForeignKey('Proxy', on_delete=models.SET_DEFAULT, default='default proxy')

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.name


class Proxy(models.Model):
    # id = models.IntegerField(primary_key=True)
    proxy = models.CharField(max_length=40, unique=True)

    class Meta:
        db_table = 'proxies'

    def __str__(self):
        return self.proxy
