# Generated by Django 5.0.1 on 2024-01-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='banner',
            field=models.ImageField(default=1, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
