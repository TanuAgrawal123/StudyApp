# Generated by Django 2.2.13 on 2020-06-15 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='email',
        ),
    ]
