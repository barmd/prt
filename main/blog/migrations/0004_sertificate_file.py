# Generated by Django 5.0.1 on 2024-01-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_info_banner_alter_info_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='sertificate',
            name='file',
            field=models.FileField(default=1, upload_to='files/'),
            preserve_default=False,
        ),
    ]
