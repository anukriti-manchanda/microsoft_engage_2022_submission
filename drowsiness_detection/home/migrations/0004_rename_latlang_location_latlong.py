# Generated by Django 4.0.4 on 2022-05-27 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_location_latlang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='latlang',
            new_name='latlong',
        ),
    ]