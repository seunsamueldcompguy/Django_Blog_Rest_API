# Generated by Django 3.0.2 on 2020-07-27 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_API', '0002_auto_20200727_0403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
