# Generated by Django 3.0.1 on 2020-11-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestingApp', '0006_education_especialty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, verbose_name='habilidad')),
                ('skill_icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_name', models.CharField(max_length=50)),
            ],
        ),
    ]