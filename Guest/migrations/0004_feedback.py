# Generated by Django 4.1.13 on 2023-12-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_alter_newseller_authorlicno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Bookname', models.CharField(max_length=30)),
                ('Comment', models.TextField(max_length=200)),
            ],
        ),
    ]