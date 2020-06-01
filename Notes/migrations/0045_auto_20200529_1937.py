# Generated by Django 2.2.12 on 2020-05-29 14:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notes', '0044_auto_20200528_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='disliked',
            field=models.ManyToManyField(blank=True, related_name='papersdisliked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='papers',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='papersliked', to=settings.AUTH_USER_MODEL),
        ),
    ]
