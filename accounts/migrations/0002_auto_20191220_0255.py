# Generated by Django 2.2 on 2019-12-20 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_ID',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
