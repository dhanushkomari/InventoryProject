# Generated by Django 3.1.4 on 2021-09-23 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0006_remove_component_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentcategory',
            name='slug',
        ),
    ]
