# Generated by Django 2.2.13 on 2020-06-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0003_auto_20200623_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
