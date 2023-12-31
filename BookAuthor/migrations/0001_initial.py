# Generated by Django 4.1.13 on 2023-12-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_cover_image', models.ImageField(upload_to='book_covers/')),
                ('author_name', models.CharField(max_length=100)),
                ('author_image', models.ImageField(upload_to='author_images/')),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('book_description', models.TextField()),
                ('book_category', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Science Fiction', 'Science Fiction'), ('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Fantasy', 'Fantasy'), ('Biography', 'Biography')], max_length=100)),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_email', models.EmailField(max_length=254)),
                ('seller_phone', models.CharField(max_length=15)),
                ('seller_description', models.TextField()),
                ('seller_location', models.CharField(max_length=100)),
                ('seller_license_number', models.CharField(max_length=50)),
            ],
        ),
    ]
