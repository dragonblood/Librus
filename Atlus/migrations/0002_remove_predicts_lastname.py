# Generated by Django 2.2.5 on 2019-12-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atlus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predicts',
            name='lastname',
        ),
    ]