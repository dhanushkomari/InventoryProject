# Generated by Django 3.1.4 on 2021-09-23 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_auto_20210827_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'ordering': ('id', 'name', 'category'), 'verbose_name': 'Components'},
        ),
    ]
