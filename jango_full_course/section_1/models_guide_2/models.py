from django.db import models


# from djongo import models


# Create your models here.
# class Dean(models.Model):
#     int_value = models.IntegerField(null=True, blank=True)
#     str_value = models.CharField(max_length=30, null=True, blank=True)
#
#     def __str__(self):
#         return 'Int is %s , str is %s' % (self.int_value, self.str_value)


class Person(models.Model):
    mother = models.ForeignKey('self', on_delete=models.CASCADE, null=True,  blank=True)
    siblings = models.ManyToManyField('self', null=True, related_name='ssiblings', blank=True)
    # partner = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True, related_name='ppartner')
    name = models.CharField(max_length=20, default='ss')

    def __str__(self):
        return 'name:%s' % self.name


# class Test(models.Model):
#     name = models.CharField(max_length=20)
