# Generated by Django 2.2.12 on 2020-05-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0013_auto_20200516_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='year',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
        migrations.AlterField(
            model_name='papers',
            name='batch',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
