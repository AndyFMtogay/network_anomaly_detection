# Generated by Django 2.1.2 on 2018-12-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nt_resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catnormalresource',
            name='click_num',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
