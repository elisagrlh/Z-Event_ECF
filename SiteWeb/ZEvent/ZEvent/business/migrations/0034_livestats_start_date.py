# Generated by Django 4.1.13 on 2024-05-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0033_delete_linkclick'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestats',
            name='start_date',
            field=models.DateTimeField(default=3),
            preserve_default=False,
        ),
    ]
