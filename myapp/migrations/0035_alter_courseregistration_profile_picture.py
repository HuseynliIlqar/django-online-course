# Generated by Django 5.2 on 2025-05-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_alter_courseregistration_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='static/img/'),
        ),
    ]
