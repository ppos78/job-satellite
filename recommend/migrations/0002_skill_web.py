# Generated by Django 3.1.5 on 2021-01-31 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='web',
            field=models.IntegerField(default=0),
        ),
    ]