# Generated by Django 5.0.6 on 2024-06-11 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_type_is'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='type_is',
            new_name='type',
        ),
    ]