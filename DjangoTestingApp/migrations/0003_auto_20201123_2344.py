# Generated by Django 3.0.1 on 2020-11-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestingApp', '0002_auto_20201123_2336'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]
