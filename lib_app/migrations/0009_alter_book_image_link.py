# Generated by Django 4.0 on 2021-12-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0008_alter_book_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_link',
            field=models.TextField(null=True),
        ),
    ]
