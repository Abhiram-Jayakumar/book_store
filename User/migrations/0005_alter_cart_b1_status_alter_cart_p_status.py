# Generated by Django 4.1.13 on 2023-12-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='b1_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='p_status',
            field=models.BooleanField(default=False),
        ),
    ]