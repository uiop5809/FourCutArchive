# Generated by Django 4.0.6 on 2022-08-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='keyword',
            field=models.CharField(choices=[('TEMP', 'temp'), ('TEST', 'test'), ('HI', 'hi')], max_length=50, verbose_name='키워드'),
        ),
    ]
