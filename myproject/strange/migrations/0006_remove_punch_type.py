# Generated by Django 4.0.5 on 2022-06-05 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strange', '0005_rename_time_punch_time_in_punch_time_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='punch',
            name='type',
        ),
    ]