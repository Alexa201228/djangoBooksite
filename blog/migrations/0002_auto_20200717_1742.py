# Generated by Django 3.0.8 on 2020-07-17 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='stug',
            new_name='slug',
        ),
    ]
