# Generated by Django 4.0.6 on 2022-08-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommends', '0002_alter_recommend_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommend',
            name='recImage',
            field=models.ImageField(blank=True, upload_to='recommends/%Y%m%d', verbose_name='추천사진'),
        ),
    ]
