# Generated by Django 3.1.4 on 2021-09-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_leave_total_no_of_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='date_of_apply',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]