from django.http import HttpResponse
from django.shortcuts import redirect, render

from Guest.models import  NewSeller, Newuser
from User.models import Cart
from .models import*


# Create your views here.

def authorhome(request):
    author=NewSeller.objects.get(id=request.session["sid"])
    return render(request,"BookAuthor/AuthorHome.html")



def Authorprofile(request):
    author=NewSeller.objects.get(id=request.session["sid"])
    return render(request, "BookAuthor/AuthorProfile.html",{'auth':author})

def addbook(request):
    if request.method == 'POST':
        book = Book(
            book_name=request.POST.get('bookName'),
            book_cover_image=request.FILES.get('bookImage'),
            author_name=request.POST.get('authorName'),
            author_image=request.FILES.get('authorimage'),
            book_price=request.POST.get('bookPrice'),
            book_description=request.POST.get('bookDescription'),
            book_category=request.POST.get('bookCategory'),
            seller_name=request.POST.get('sellerName'),
            seller_email=request.POST.get('sellerEmail'),
            seller_phone=request.POST.get('sellerPhone'),
            seller_description=request.POST.get('sellerDescription'),
            seller_location=request.POST.get('sellerLocation'),
            seller_license_number=request.POST.get('sellerLicense')
        )
        book.save()
    return render(request,"BookAuthor/Addbook.html")




def AddEbook(request):
    if request.method == 'POST':
        book = EBook(
            book_name=request.POST.get('bookName'),
            book_cover_image=request.FILES.get('bookImage'),
            author_name=request.POST.get('authorName'),
            book_price=request.POST.get('bookPrice'),
            book_description=request.POST.get('bookDescription'),
            book_category=request.POST.get('bookCategory'),
            seller_name=request.POST.get('sellerName'),
            author_image=request.FILES.get('authorimage'),
            seller_email=request.POST.get('sellerEmail'),
            seller_phone=request.POST.get('sellerPhone'),
            seller_description=request.POST.get('sellerDescription'),
            seller_location=request.POST.get('sellerLocation'),
            seller_license_number=request.POST.get('sellerLicense'),
            book_file=request.FILES.get('bookFile')
        )
        book.save()
    return render(request,"BookAuthor/AddEbook.html")





def seller_view_bookings(request):
    if 'sid' in request.session:
        seller_id = request.session['sid']
        seller_bookings = Cart.objects.filter(Seller_id=seller_id)
        
        context = {
            'seller_bookings': seller_bookings,
        }
        return render(request, "BookAuthor/seller_bookings.html", context)
    else:
        return HttpResponse("Seller ID not found in session. Please log in as a seller.")



def seller_added_books(request):
    if 'sid' in request.session:  
        seller_id = request.session['sid']
        physical_books = Book.objects.filter(SellerAdd_id=seller_id)
        ebooks = EBook.objects.filter(SellerEAdd_id=seller_id)

        context = {
            'physical_books': physical_books,
            'ebooks': ebooks,
        }
        return render(request, "BookAuthor/seller_added_books.html", context)
    else:
        return HttpResponse("Seller ID not found in session. Please log in as a seller.")
    
    
def update_seller_profile(request, cid):
    seller = NewSeller.objects.get(id=cid)
    
    if request.method == "POST":
        seller.Name = request.POST.get("txt_name")
        seller.Contact = request.POST.get("txt_contact")
        seller.Email = request.POST.get("txt_email")
        seller.Address = request.POST.get("txt_address")
        seller.Registername = request.POST.get("txt_register_name")
        seller.save()
        
        return redirect('BookAuthor:update_seller_profile', cid=seller.id)
    
    return render(request, "BookAuthor/Sellerupdate_profile.html", {"seller": seller})




def Seller_update_password(request, cid):
    try:
        seller = NewSeller.objects.get(id=cid)
    except NewSeller.DoesNotExist:
        return render(request, "User/Update_password.html", {"error_message": "User does not exist."})

    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not seller.Password == current_password:
            return render(request, "User/Update_password.html", {"error_message": "Incorrect current password."})

        if new_password != confirm_password:
            return render(request, "User/Update_password.html", {"error_message": "New passwords do not match."})

        seller.Password = new_password
        seller.save()

        return redirect('Guest:login')  

    return render(request, "User/Update_password.html", {"seller": seller})