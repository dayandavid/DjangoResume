# Generated by Django 3.0.1 on 2020-11-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestingApp', '0005_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='especialty',
            field=models.CharField(default='Especialidad', max_length=50, verbose_name='especialidad'),
            preserve_default=False,
        ),
    ]
