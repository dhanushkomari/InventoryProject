# Generated by Django 3.1.4 on 2021-09-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_remove_componentcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='invoice',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
