# Generated by Django 3.2.10 on 2021-12-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211216_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='gold_tickets',
        ),
        migrations.RemoveField(
            model_name='event',
            name='premium_tickets',
        ),
        migrations.RemoveField(
            model_name='event',
            name='standard',
        ),
        migrations.RemoveField(
            model_name='event',
            name='total_tickets',
        ),
        migrations.AddField(
            model_name='ticket',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
