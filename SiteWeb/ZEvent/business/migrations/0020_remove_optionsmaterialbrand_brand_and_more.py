# Generated by Django 5.0.3 on 2024-05-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0019_alter_live_material_brands_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionsmaterialbrand',
            name='brand',
        ),
        migrations.AddField(
            model_name='optionsmaterialbrand',
            name='brand',
            field=models.ManyToManyField(max_length=300, to='business.optionsmateriallabel'),
        ),
    ]
