# Generated by Django 2.0.4 on 2018-04-23 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='blog.Blog'),
        ),
    ]
