# Generated by Django 4.1.5 on 2023-03-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Item/foodpicture'),
        ),
    ]
