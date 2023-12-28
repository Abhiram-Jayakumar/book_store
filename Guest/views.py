from django.shortcuts import get_object_or_404, redirect, render
from Admin.models import Admintable

from BookAuthor.models import Book, EBook
from User.models import Review
from .models import*


def login(request):
    if request.method=="POST":
        email=request.POST.get('logemail')
        Pass=request.POST.get('logpass')
        Ulogin=Newuser.objects.filter(Email=email,Password=Pass).count()
        Slogin=NewSeller.objects.filter(Email=email,Password=Pass,vstatus=True).count()
        Alogin=Admintable.objects.filter(admin_email=email,admin_password=Pass).count()
        if Ulogin > 0:
            uadmin=Newuser.objects.get(Email=email,Password=Pass)
            request.session['uid']=uadmin.id
            return redirect('User:userhome')
        elif Slogin > 0:
            sadmin=NewSeller.objects.get(Email=email,Password=Pass,vstatus=1)
            request.session['sid']=sadmin.id
            return redirect('BookAuthor:authorhome')
        elif Alogin > 0:
            aadmin=Admintable.objects.get(admin_email=email,admin_password=Pass)
            request.session['aid']=aadmin.id
            return redirect('Admin:AdminHome')
        else:
            error="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'ERR':error})
    else:
        return render(request, "Guest/Login.html")



def register(request):
    if request.method=='POST':
        Newuser.objects.create(Firstname=request.POST.get('first_name'),Lastname=request.POST.get('last_name'),Email=request.POST.get('user_email'),
         Street=request.POST.get('street'),Address=request.POST.get('address'),Zipcode=request.POST.get('zip_code'),
         Place=request.POST.get('place'),Country=request.POST.get('country'),PhnCode=request.POST.get('ph_code'),PhnNumber=request.POST.get('phn_number'),
         Password=request.POST.get('password'))
        return render(request,"Guest/Thankyou.html")
    else:
        register=Newuser.objects.all()
        return render(request,"Guest/Register.html")
    
        

def sellerregister(request):
    if request.method == "POST":
        NewSeller.objects.create(
            Name=request.POST.get('txt_name'),
            Contact=request.POST.get('txt_contact'),
            Email=request.POST.get('txt_email'),
            Address=request.POST.get('txt_address'),
            Registername=request.POST.get('txt_registername'),
            AuthorLicno=request.POST.get('txt_licensenumber'),
            Proof1=request.POST.get('image_proof1'),
            Proof2=request.POST.get('image_proof2'),  
            Password=request.POST.get('password')
        )
        return render(request, "Guest/Thankyou.html")
    else:
        sellerregister=NewSeller.objects.all()
        return render(request, "Guest/Seller.html")



def index(request):
    viewbook=Book.objects.all()
    return render(request,"Guest/index.html",{'data':viewbook})




def Thankyou(request):
    return render(request, "Guest/ThankYou.html")




def Productd(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "Guest/Product.html", {'book': book})

def ebook_list(request):
    ebooks = EBook.objects.all()
    return render(request, "Guest/Ebook.html", {'ebooks': ebooks})

def Ebookdisp(request, bbook_id):
    ebook = get_object_or_404(EBook, pk=bbook_id)
    return render(request, "Guest/Ebookdisplay.html", {'ebook': ebook})

def book_seller_info(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "Guest/book_seller_info.html", {'book': book})

def displayreviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_reviews = Review.objects.filter(Bookdetail_id=book_id)
    return render(request, "Guest/GuestViewReview.html", {'book_reviews': book_reviews, 'book_name': book.book_name})

def Guest_author_detail_view(request, ebook_id):
    ebook = get_object_or_404(EBook, pk=ebook_id)
    return render(request, 'Guest/EGuestAuthor.html', {'ebook': ebook})

def Guest_view_ebook_reviews(request, ebook_id):
    ebook =EBook.objects.get(pk=ebook_id)
    reviews = Review.objects.filter(EBookdetail=ebook)
    
    return render(request, "Guest/GuestEViewReview.html", {'ebook': ebook, 'reviews': reviews})

