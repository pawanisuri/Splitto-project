# Generated by Django 2.2.6 on 2019-11-24 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('splitapp', '0003_auto_20191123_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]