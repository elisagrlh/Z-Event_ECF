# Generated by Django 5.0.3 on 2024-04-13 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0011_alter_userdata_email_alter_userdata_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='username',
        ),
    ]