# Generated by Django 2.0.4 on 2018-05-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20180513_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, default='pass', to='blog.Tag'),
        ),
    ]
