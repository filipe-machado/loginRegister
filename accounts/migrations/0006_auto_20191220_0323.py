# Generated by Django 2.2 on 2019-12-20 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191220_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default='2000-10-10'),
        ),
    ]