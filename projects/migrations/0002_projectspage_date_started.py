# Generated by Django 3.1.4 on 2021-01-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectspage',
            name='date_started',
            field=models.DateField(),
        ),
    ]
