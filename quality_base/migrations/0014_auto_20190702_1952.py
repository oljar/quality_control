# Generated by Django 2.0.6 on 2019-07-02 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_base', '0013_amber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='controller',
        ),
        migrations.RemoveField(
            model_name='check',
            name='unit_type',
        ),
        migrations.RemoveField(
            model_name='amber',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='amber',
            name='unit_type',
        ),
        migrations.DeleteModel(
            name='AHU',
        ),
        migrations.DeleteModel(
            name='Check',
        ),
    ]
