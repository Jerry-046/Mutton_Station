# Generated by Django 4.1.5 on 2023-03-28 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0005_rename_name_category_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
    ]