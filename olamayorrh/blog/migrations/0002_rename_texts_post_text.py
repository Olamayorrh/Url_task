# Generated by Django 4.0.5 on 2022-06-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='texts',
            new_name='text',
        ),
    ]
