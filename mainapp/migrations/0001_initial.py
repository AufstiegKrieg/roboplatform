# Generated by Django 3.1.3 on 2020-11-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='урок')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
    ]
