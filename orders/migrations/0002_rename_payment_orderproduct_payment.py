# Generated by Django 4.1.3 on 2022-11-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='Payment',
            new_name='payment',
        ),
    ]
