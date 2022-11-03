# Generated by Django 3.2.8 on 2022-08-28 10:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='users',
        ),
        migrations.AddField(
            model_name='film',
            name='users',
            field=models.ManyToManyField(related_name='films', to=settings.AUTH_USER_MODEL),
        ),
    ]
