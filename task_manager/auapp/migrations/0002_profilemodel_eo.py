# Generated by Django 3.2.6 on 2021-12-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='eo',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
