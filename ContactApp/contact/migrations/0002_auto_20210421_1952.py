# Generated by Django 3.2 on 2021-04-21 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
