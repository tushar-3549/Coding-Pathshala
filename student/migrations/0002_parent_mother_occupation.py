# Generated by Django 5.1.7 on 2025-04-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='mother_occupation',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
