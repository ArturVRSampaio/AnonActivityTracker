# Generated by Django 4.2.11 on 2024-03-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
