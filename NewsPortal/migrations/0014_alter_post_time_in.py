# Generated by Django 4.0.3 on 2022-09-06 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0013_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 6, 8, 14, 3, 155290)),
        ),
    ]