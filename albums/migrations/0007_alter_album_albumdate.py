# Generated by Django 4.0.6 on 2022-08-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_album_albumdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='albumdate',
            field=models.DateField(null=True, verbose_name='앨범날짜'),
        ),
    ]
