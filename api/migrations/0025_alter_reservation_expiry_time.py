# Generated by Django 3.2.10 on 2021-12-18 01:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_alter_reservation_expiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 1, 43, 57, 913203)),
        ),
    ]
