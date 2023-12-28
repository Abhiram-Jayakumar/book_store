from django.db import models

from Guest.models import NewSeller


class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Biography', 'Biography'),
    ]

    book_name = models.CharField(max_length=100)
    book_cover_image = models.ImageField(upload_to='book_covers/')
    author_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images/')
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_description = models.TextField()
    book_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=15)
    seller_description = models.TextField()
    seller_location = models.CharField(max_length=100)
    seller_license_number = models.CharField(max_length=50)
    SellerAdd=models.ForeignKey(NewSeller,on_delete=models.SET_NULL,null=True)



class EBook(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'),
        ('Thriller', 'Thriller'),
        ('Fantasy', 'Fantasy'),
        ('Biography', 'Biography'),
    ]

    book_name = models.CharField(max_length=100)
    book_cover_image = models.ImageField(upload_to='book_covers/')
    author_name = models.CharField(max_length=100)
    book_price = models.DecimalField(max_digits=10, decimal_places=2)
    book_description = models.TextField()
    book_category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    seller_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images/')
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=15)
    seller_description = models.TextField()
    seller_location = models.CharField(max_length=100)
    seller_license_number = models.CharField(max_length=50)
    book_file = models.FileField(upload_to='ebooks/', blank=True, null=True)
    SellerEAdd=models.ForeignKey(NewSeller,on_delete=models.SET_NULL,null=True)
