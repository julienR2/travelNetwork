# Generated by Django 2.0 on 2018-03-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]