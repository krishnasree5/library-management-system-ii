# Generated by Django 5.0.6 on 2024-06-14 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]
