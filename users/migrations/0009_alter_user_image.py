# Generated by Django 4.0.6 on 2022-08-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y%m%d', verbose_name='프로필사진'),
        ),
    ]
