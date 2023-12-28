from django.db import models
from BookAuthor.models import Book, EBook

from Guest.models import NewSeller, Newuser

# Create your models here.
class Cart(models.Model):
    Bookbooking=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    EBookbooking=models.ForeignKey(EBook,on_delete=models.SET_NULL,null=True)
    Booking1_Date=models.DateField(auto_now=True)
    b1_status = models.BooleanField(default=True)
    p_status = models.BooleanField(default=True)
    User1=models.ForeignKey(Newuser,on_delete=models.SET_NULL,null=True)
    Seller = models.ForeignKey(NewSeller, on_delete=models.SET_NULL, null=True)
    
    
        
class Review(models.Model):
    RATING_CHOICES = [
        (5, 'Excellent'),
        (4, 'Very Good'),
        (3, 'Good'),
        (2, 'Fair'),
        (1, 'Poor'),
    ]
    Bookdetail=models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    EBookdetail=models.ForeignKey(EBook,on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()