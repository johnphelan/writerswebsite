# Generated by Django 3.1.5 on 2021-07-31 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210729_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
