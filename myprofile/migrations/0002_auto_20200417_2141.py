# Generated by Django 3.0.5 on 2020-04-17 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='addr1',
        ),
    ]
