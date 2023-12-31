# Generated by Django 4.1.13 on 2023-12-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_type', models.CharField(choices=[('Service', 'Service'), ('Product', 'Product'), ('Delivery', 'Delivery'), ('Others', 'Others')], max_length=20)),
                ('complaint_details', models.TextField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=15)),
            ],
        ),
    ]
