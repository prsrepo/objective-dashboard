# Generated by Django 3.0.8 on 2020-07-18 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objectives_dashboard', '0002_auto_20200718_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='date_of_innaugration',
            new_name='date_of_inauguration',
        ),
    ]
