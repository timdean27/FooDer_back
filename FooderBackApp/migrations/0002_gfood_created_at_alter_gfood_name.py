# Generated by Django 4.0.6 on 2022-07-14 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FooderBackApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gfood',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gfood',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]