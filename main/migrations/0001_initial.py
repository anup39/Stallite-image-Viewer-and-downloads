# Generated by Django 3.1.3 on 2020-12-03 18:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('raster', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
    ]
