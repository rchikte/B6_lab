# Generated by Django 4.0.1 on 2022-01-29 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0002_book_auth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='auth',
        ),
    ]