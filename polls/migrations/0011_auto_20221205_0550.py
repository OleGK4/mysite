# Generated by Django 3.2.16 on 2022-12-05 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20221205_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='is_activated',
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
    ]
