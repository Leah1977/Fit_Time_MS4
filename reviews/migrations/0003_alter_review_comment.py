# Generated by Django 3.2.9 on 2021-12-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211204_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, default=0),
        ),
    ]
