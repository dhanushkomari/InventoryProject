# Generated by Django 3.1.4 on 2021-09-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='total_no_of_leaves',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
