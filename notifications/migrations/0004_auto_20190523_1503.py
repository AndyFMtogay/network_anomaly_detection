# Generated by Django 2.1.7 on 2019-05-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('notifications', '0003_auto_20190503_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间'),
        ),
    ]