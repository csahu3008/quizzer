# Generated by Django 2.2.3 on 2019-08-01 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190801_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizzers',
            name='password1',
            field=models.CharField(default='emialhf', max_length=40, verbose_name='Password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quizzers',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
