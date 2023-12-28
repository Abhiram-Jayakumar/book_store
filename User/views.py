from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from BookAuthor.models import Book, EBook
from Guest.models import  Complaint, Newuser
from User.models import Cart,Review
from django.contrib.auth.hashers import check_password, make_password
from datetime import timedelta

# Create your views here.
def homeuser(request):
    Viewbook=Book.objects.all()
    return render(request, "User/Homepage.html",{'data':Viewbook})

def complaint(request):
    if request.method == 'POST':
        complaint_type = request.POST.get('complaintType')
        complaint_details = request.POST.get('complaintDetails')
        customer_name = request.POST.get('customerName')
        customer_email = request.POST.get('customerEmail')
        customer_phone = request.POST.get('customerPhone')

        new_complaint = Complaint(
            complaint_type=complaint_type,
            complaint_details=complaint_details,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone
        )
        new_complaint.save()
    return render(request, "User/Complaint.html")


def cart_view(request, cid):
    if "uid" in request.session:
        toi = Book.objects.get(id=cid)
        
        seller = toi.SellerAdd 
        
        con1 = Book.objects.filter(id=cid)
        
        if request.method == 'POST':
            userobj = Newuser.objects.get(id=request.session["uid"])
            
            Cart.objects.create(Bookbooking=toi, User1=userobj, Seller=seller)
            
            conb = Cart.objects.all()
            return render(request, 'User/Cart.html', {"i": toi, "userobj": userobj, "conb": conb, "con1": con1, "user_id": cid})
        else:
            toi = Book.objects.get(id=cid)
            return render(request, 'User/Cart.html', {"i": toi, "con1": con1})
    else:
        return redirect('User:userhome')
     
     
     
def updateuser(request,cid):
    userupd=Newuser.objects.get(id=request.session["uid"])
    booked=Cart.objects.filter(User1=userupd)
    if request.method=="POST" :
       userupd.Firstname=request.POST.get("txt_firstname") 
       userupd.Lastname=request.POST.get("txt_lastname") 
       userupd.Email=request.POST.get("txt_email") 
       userupd.Street=request.POST.get("txt_street") 
       userupd.Address=request.POST.get("txt_address")
       userupd.Zipcode=request.POST.get("txt_zipcode")
       userupd.Place=request.POST.get("txt_place")
       userupd.Country=request.POST.get("txt_country")
       
       userupd.PhnNumber=request.POST.get("txt_phnNumber")
       userupd.save()
       return redirect('User:Updateuser', cid=userupd.id)

    else:
        return render(request,"User/Editadress.html",{"userupd":userupd,"booked":booked})



def userdetails(request):
    userupd = Newuser.objects.get(id=request.session.get("uid"))
    return render(request, "User/Userprofile.html", {"details": userupd, "userupd": userupd})



def payment(request, pid):
    if "uid" in request.session:  
        pay = Cart.objects.get(id=pid)
        if request.method == 'POST':
            hid = request.POST.get("hidden")
            pay = Cart.objects.get(id=hid)
            pay.p_status = True
            pay.save()
            return redirect('User:tnxshop')
        else:
            return render(request, "User/Payment.html", {"pay": pay})
    else:
        return redirect('Guest:login')


def tnxshop(request):
    return render(request, "User/Thankyoushopping.html")


def Productdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "User/Productdetail.html", {'book': book})


def view_booking(request):
    user_id = request.session.get("uid")
    if user_id:
        user_carts = Cart.objects.filter(User1_id=user_id)
        return render(request, "User/UserBooking.html", {'booking_details1': user_carts})
    else:
        return redirect('User:userhome')
   
   
    
def ebooklistUser(request):
    ebooks = EBook.objects.all()
    return render(request, "User/Ebookuser.html", {'ebooks': ebooks})



def EbookdispUser(request, bbook_id):
    ebook = get_object_or_404(EBook, pk=bbook_id)
    return render(request, "User/Ebookuser_display.html", {'ebook': ebook})



def book_sellerinfo(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "User/Authorinfo.html", {'book': book})






def review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        new_review = Review(Bookdetail=book, rating=rating, comment=comment)
        new_review.save()
    
    return render(request, "User/AddReview.html",{'book_name': book.book_name})





def display_reviews(request, book_id):
    book = Book.objects.get(pk=book_id)
    book_reviews = Review.objects.filter(Bookdetail_id=book_id)
    return render(request, "User/ViewReview.html", {'book_reviews': book_reviews, 'book_name': book.book_name})




def Ecart_view(request, bbook_id):
    if "uid" in request.session:
        toi = get_object_or_404(EBook, id=bbook_id)
        
        seller = toi.SellerEAdd  
        
        con1 = EBook.objects.filter(id=bbook_id)

        if request.method == 'POST':
            userobj = get_object_or_404(Newuser, id=request.session["uid"])

            pay = Cart.objects.create(EBookbooking=toi, User1=userobj, Seller=seller)
            return redirect('User:Epayment', pid=pay.id)
        else:
            return render(request, 'User/Ecart.html', {"i": toi, "con1": con1})
    else:
        return redirect('User:userhome')



def Epayment(request, pid):
    if "uid" in request.session:
        pay = get_object_or_404(Cart, id=pid)

        if request.method == 'POST':
            pay.p_status = True
            pay.save()
            return redirect('User:payment_success', pid=pay.id)
        else:
            return render(request, "User/EPayment.html", {"pay": pay})
    else:
        return redirect('Guest:login')
    
    
def payment_success(request, pid):
    pay = get_object_or_404(Cart, id=pid)
    
    context = {'pay': pay}
    return render(request, 'User/PaymentSuccess.html', context)



def download_ebook(request, pid):
    pay = get_object_or_404(Cart, id=pid)
    ebook = pay.EBookbooking.book_file

    if ebook:
        response = HttpResponse(ebook.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(pay.EBookbooking.book_name)
        return response
    else:
        return HttpResponse("E-book file not found.")
 
    
    
def author_detail_view(request, ebook_id):
    ebook = get_object_or_404(EBook, pk=ebook_id)
    return render(request, 'User/Eauthor_detail.html', {'ebook': ebook})



def update_profile(request, cid):
    userupd = Newuser.objects.get(id=cid)
    
    if request.method == "POST":
        userupd.Firstname = request.POST.get("txt_firstname")
        userupd.Lastname = request.POST.get("txt_lastname")
        userupd.Email = request.POST.get("txt_email")
        userupd.Street = request.POST.get("txt_street")
        userupd.Address = request.POST.get("txt_address")
        userupd.Zipcode = request.POST.get("txt_zipcode")
        userupd.Place = request.POST.get("txt_place")
        userupd.Country = request.POST.get("txt_country")
        userupd.PhnNumber = request.POST.get("txt_phnNumber")
        
        userupd.save()
        return redirect('User:update_profile', cid=userupd.id)
    
    return render(request, "User/update_profile.html", {"userupd": userupd})

    

def update_password(request, cid):
    try:
        user = Newuser.objects.get(id=cid)
    except Newuser.DoesNotExist:
        return render(request, "User/update_password.html", {"error_message": "User does not exist."})

    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not user.Password == current_password:
            return render(request, "User/update_password.html", {"error_message": "Incorrect current password."})

        if new_password != confirm_password:
            return render(request, "User/update_password.html", {"error_message": "New passwords do not match."})

        user.Password = new_password
        user.save()

        return redirect('Guest:login')  

    return render(request, "User/update_password.html", {"user": user})





def track_order(request, booking_id):
    booking = get_object_or_404(Cart, id=booking_id)

    booking.Booking1_Date_plus_2_days = booking.Booking1_Date + timedelta(days=2)
    booking.Booking1_Date_plus_1_days = booking.Booking1_Date + timedelta(days=1)

    context = {'booking': booking} 

    return render(request, "User/Trackorder.html", {'booking': booking, 'context': context})



def view_order_details(request, booking_id):
    cart = Cart.objects.get(id=booking_id)
    context = {
        'book_name': cart.Bookbooking.book_name if cart.Bookbooking else None,
        'book_price': cart.Bookbooking.book_price if cart.Bookbooking else None,
        'book_description': cart.Bookbooking.book_description if cart.Bookbooking else None,
        'book_category': cart.Bookbooking.book_category if cart.Bookbooking else None,
        'author_name': cart.Bookbooking.author_name if cart.Bookbooking else None,    }
    return render(request, 'User/order_details.html', context)


def add_ebook_review(request, ebook_id):
    ebook = get_object_or_404(EBook, pk=ebook_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        new_review = Review(EBookdetail=ebook, rating=rating, comment=comment)
        new_review.save()
    
    return render(request, "User/EAddReview.html", {'ebook': ebook})



def view_ebook_reviews(request, ebook_id):
    ebook =EBook.objects.get(pk=ebook_id)
    reviews = Review.objects.filter(EBookdetail=ebook)
    
    return render(request, "User/EViewReview.html", {'ebook': ebook, 'reviews': reviews})
