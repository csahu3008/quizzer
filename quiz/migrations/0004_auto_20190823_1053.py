# Generated by Django 2.2.4 on 2019-08-23 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190823_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='stud_appeared',
            new_name='studs',
        ),
    ]
