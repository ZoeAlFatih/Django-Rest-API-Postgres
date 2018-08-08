# Generated by Django 2.1 on 2018-08-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='message',
            name='to_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='senders',
            name='from_phone',
            field=models.CharField(max_length=15),
        ),
    ]