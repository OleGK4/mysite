# Generated by Django 3.2.16 on 2022-12-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_question_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
