# Generated by Django 3.2.16 on 2022-12-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_delete_advuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='photo',
            field=models.ImageField(default='image', upload_to='question_img'),
        ),
    ]
