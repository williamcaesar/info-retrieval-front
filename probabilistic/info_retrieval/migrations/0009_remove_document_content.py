# Generated by Django 2.0.5 on 2018-05-13 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_retrieval', '0008_auto_20180513_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='content',
        ),
    ]
