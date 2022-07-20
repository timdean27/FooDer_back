# Generated by Django 4.0.6 on 2022-07-19 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gfood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_string', models.CharField(default='unknown_user', max_length=100)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Gfood', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
