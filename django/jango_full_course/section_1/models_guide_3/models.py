from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def is_even(value):
    if (value % 2 != 0):
        raise ValidationError(str(value) + " is not even")


class EvenInteger(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(is_even)


class MyModel(models.Model):
    even_id = models.IntegerField(validators=[is_even])
    custom_even_id = EvenInteger()


class Person_3(models.Model):
    birth_year = models.IntegerField()

    # objects =models.Manager() this is the default manager Person_3.objects.all()
    people = models.Manager()  # Person_3.people.all()

    def __str__(self):
        return self.birth_year

    class Meta:
        ordering = ['birth_year']
        db_table = 'person'


class Person_4(models.Model):
    birth_year = models.IntegerField()
    death_year = models.IntegerField()

    def before_hundered(self):
        if self.birth_year < 100:
            return True
        return False

    def save(self, *args, **kwargs):
        if self.birth_year > 100:
            super().save(*args, **kwargs)
        else:
            print("Too old!")
            return

    def __str__(self):
        return f'{self.birth_year}:{self.death_year}'
