# Generated by Django 2.1.2 on 2018-10-06 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0018_remove_estimated_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testruntag',
            name='user',
        ),
    ]
