# Generated by Django 4.0 on 2021-12-22 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0002_remove_libdata_profile_libdata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libdata',
            name='user',
        ),
    ]
