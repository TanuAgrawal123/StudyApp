# Generated by Django 2.2.12 on 2020-05-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0016_auto_20200516_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='data',
            field=models.FileField(upload_to='document/'),
        ),
    ]