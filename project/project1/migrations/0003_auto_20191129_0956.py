# Generated by Django 2.2.7 on 2019-11-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0002_auto_20191129_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asanauser',
            name='asana_id',
            field=models.CharField(max_length=50),
        ),
    ]
