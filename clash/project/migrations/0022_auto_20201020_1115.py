# Generated by Django 3.1 on 2020-10-20 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_register_quefulllist'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='getassured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='register',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
