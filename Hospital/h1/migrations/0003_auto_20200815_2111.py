# Generated by Django 3.0 on 2020-08-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h1', '0002_auto_20200815_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Hospital',
            new_name='hospital',
        ),
    ]
