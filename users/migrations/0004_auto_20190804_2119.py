# Generated by Django 2.2.3 on 2019-08-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190801_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzers',
            name='is_stud',
            field=models.BooleanField(default=False, verbose_name='Stud'),
        ),
    ]
