# Generated by Django 2.2.12 on 2020-05-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0007_auto_20200513_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='branch',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
