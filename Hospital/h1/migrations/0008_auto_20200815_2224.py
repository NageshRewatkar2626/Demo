# Generated by Django 3.0 on 2020-08-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h1', '0007_auto_20200815_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='hospital',
            new_name='hospital_id',
        ),
    ]
