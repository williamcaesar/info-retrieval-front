# Generated by Django 2.0.5 on 2018-05-13 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_retrieval', '0011_document_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='content',
        ),
    ]
