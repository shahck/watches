# Generated by Django 4.1.3 on 2022-11-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='userprofile'),
        ),
    ]