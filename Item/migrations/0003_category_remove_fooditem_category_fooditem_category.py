# Generated by Django 4.1.5 on 2023-03-27 06:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0002_alter_fooditem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='category',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='category',
            field=models.ManyToManyField(blank=True, to='Item.category'),
        ),
    ]
