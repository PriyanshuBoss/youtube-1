# Generated by Django 3.2 on 2021-04-14 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchdetail',
            name='query',
        ),
    ]
