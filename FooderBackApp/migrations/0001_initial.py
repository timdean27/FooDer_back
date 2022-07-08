# Generated by Django 4.0.6 on 2022-07-08 21:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gfood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.TextField()),
                ('Liked_Foods', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
                ('disLiked_Foods', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, size=None)),
            ],
        ),
    ]