# Generated by Django 2.2.12 on 2020-05-18 14:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Notes', '0028_auto_20200518_1948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Student',
        ),
    ]
