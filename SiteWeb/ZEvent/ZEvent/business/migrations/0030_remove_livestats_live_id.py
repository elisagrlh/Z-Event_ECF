# Generated by Django 4.1.13 on 2024-05-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0029_linkclick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestats',
            name='live_id',
        ),
    ]
