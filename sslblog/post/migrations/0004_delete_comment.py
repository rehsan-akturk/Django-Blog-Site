# Generated by Django 3.0.8 on 2020-07-08 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
