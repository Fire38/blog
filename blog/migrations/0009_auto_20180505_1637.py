# Generated by Django 2.0.4 on 2018-05-05 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20180424_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='article',
            name='blog',
        ),
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
