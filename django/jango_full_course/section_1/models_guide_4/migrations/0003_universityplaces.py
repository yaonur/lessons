# Generated by Django 4.0.5 on 2022-07-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_guide_4', '0002_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityPlaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
