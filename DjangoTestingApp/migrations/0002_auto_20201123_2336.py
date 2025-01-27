# Generated by Django 3.0.1 on 2020-11-24 07:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoTestingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('profile_pic', models.ImageField(upload_to='profileImages', verbose_name='Profile Picture')),
            ],
        ),
        migrations.AlterField(
            model_name='jobexperience',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobexperience',
            name='job_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoTestingApp.JobPosition'),
        ),
        migrations.AlterField(
            model_name='jobexperience',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoTestingApp.Profile')),
            ],
        ),
    ]
