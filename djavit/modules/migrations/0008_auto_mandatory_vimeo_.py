# Generated by Django 3.0.8 on 2020-07-21 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_classs_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classs',
            name='vimeo_id',
            field=models.CharField(max_length=32),
        ),
    ]
