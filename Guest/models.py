from django.db import models



class Newuser(models.Model):
        Firstname=models.CharField(max_length=30)
        Lastname=models.CharField(max_length=30)
        Email=models.EmailField(unique=True)
        Street=models.CharField(max_length=30)
        Address=models.TextField(unique=True)
        Zipcode=models.CharField(max_length=30)
        Place=models.CharField(max_length=30)
        Country=models.CharField(max_length=30)
        PhnCode=models.CharField(max_length=20)
        PhnNumber=models.CharField(max_length=15)
        Password=models.CharField(unique=True,max_length=20)
        
        
        
class NewSeller(models.Model):
        Name=models.CharField(max_length=30)
        Contact=models.CharField(max_length=20)
        Email=models.EmailField(unique=True)
        Address=models.TextField(unique=True)
        Registername=models.CharField(max_length=30)
        AuthorLicno=models.CharField(max_length=20)
        Proof1 = models.CharField(max_length=20,)
        Proof2 = models.CharField(max_length=20,)
        Password=models.CharField(unique=True,max_length=20)
        vstatus=models.IntegerField(default=0)

        

        
        

    
    




class Complaint(models.Model):
    COMPLAINT_CHOICES = [
        ('Service', 'Service'),
        ('Product', 'Product'),
        ('Delivery', 'Delivery'),
        ('Others', 'Others'),
    ]

    complaint_type = models.CharField(max_length=20, choices=COMPLAINT_CHOICES, default='Others')
    complaint_details = models.TextField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)