from django.db import models


# Create your models here.
# class User(models.Model):
#     email = models.CharField(max_length=30, primary_key=True)
#     first_name = models.CharField(max_length=20, null=True, verbose_name="First")
#     second_name = models.CharField(max_length=20, default="Doe")
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other')
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
#
#
# class Dean(models.Model):
#     pass
#
#
# class Teacher(models.Model):
#     pass
#
#
# class Diploma(models.Model):
#     pass
#
#
# class Student(models.Model):
#     dean = models.ForeignKey(Dean, on_delete=models.CASCADE)
#     teachers = models.ManyToManyField(Teacher, )
#     diploma = models.OneToOneField(Diploma, on_delete=models.CASCADE)


# Dean_jack = Dean.objects.create()
#
# Teacher_1 = Teacher.objects.create()
# Teacher_2 = Teacher.objects.create()
#
# Diploma1 = Diploma.objects.create()
# Diploma2 = Diploma.objects.create()
#
# Student1 = Student.objects.create(dean=Dean_jack, diploma=Diploma1)
# Student2 = Student.objects.create(dean=Dean_jack, diploma=Diploma2)
#
# Student1.teachers.add(Teacher_1)
# Student1.teachers.add(Teacher_2)
# Student2.teachers.add(Teacher_1)
# models_guide_user:
#    id
#    first_name
#    second_name
