# Generated by Django 3.1.4 on 2021-09-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('requested', 'requested'), ('approve', 'approve'), ('decline', 'decline'), ('deploy', 'deploy')], default='requested', max_length=50),
        ),
    ]
