# Generated by Django 2.1.7 on 2019-03-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190303_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
