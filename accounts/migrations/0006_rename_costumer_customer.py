# Generated by Django 3.2.8 on 2021-11-19 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211118_2356'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumer',
            new_name='Customer',
        ),
    ]