# Generated by Django 2.1.1 on 2018-09-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_remove_board_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdby',
            field=models.CharField(max_length=100),
        ),
    ]
