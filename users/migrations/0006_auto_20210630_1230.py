# Generated by Django 3.1.5 on 2021-06-30 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20210628_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='accountcode',
        ),
        migrations.CreateModel(
            name='AccountAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountcode', models.CharField(default='entercodehere', max_length=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
