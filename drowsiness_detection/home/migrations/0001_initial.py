# Generated by Django 4.0.4 on 2022-05-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carNumber', models.CharField(max_length=20)),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
    ]
