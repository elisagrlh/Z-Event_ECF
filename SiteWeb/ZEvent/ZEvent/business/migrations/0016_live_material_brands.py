# Generated by Django 5.0.3 on 2024-05-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0015_remove_live_material_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='live',
            name='material_brands',
            field=models.ManyToManyField(through='business.LiveMaterial', to='business.optionsmaterialbrand'),
        ),
    ]
