# Generated by Django 5.0.3 on 2024-05-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_alter_live_streamer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='pseudo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]