from django.db import models


# Create your models here.
class UniversityPlaces(models.Model):
    name = models.CharField(max_length=100)


class Person(models.Model):
    birth_year = models.IntegerField()
    death_year = models.IntegerField()
    places = models.ManyToManyField(UniversityPlaces,
                                    related_name=f"%(app_label)s_%(class)s_related")  # models_guide_4_person_related

    class Meta:
        ordering = ['birth_year']
        abstract = True


class Student(Person):
    study_program = models.CharField(max_length=100)

    class Meta(Person.Meta):
        db_table = "students"


class Teacher(Person):
    research = models.CharField(max_length=100)
