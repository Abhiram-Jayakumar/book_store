import json
from django.db.models import Count
from django.shortcuts import redirect, render
from Guest.models import Complaint, NewSeller
from User.models import Cart
# Create your views here.

def AdminHome(request):
    return render(request, "Admin/AdminHome.html")


def view_complaints(request):
    complaints = Complaint.objects.all()
    return render(request, "Admin/View_Complaints.html", {'complaints': complaints})



def view_booking_details(request):
    booking = Cart.objects.all()  
    return render(request, "Admin/Booking.html", {'booking': booking})


def seller_approval(request):
    pending_registrations = NewSeller.objects.filter(vstatus=0)  # Fetch registrations pending for approval

    if request.method == "POST":
        seller_id = request.POST.get('seller_id')
        action = request.POST.get('action')  # 'approve' or 'reject'

        if action == 'approve':
            registration = NewSeller.objects.get(id=seller_id)
            registration.vstatus = 1  # Set vstatus to 1 to mark as approved
            registration.save()
            # Add any other actions upon approval (e.g., sending an email notification to the seller)

        elif action == 'reject':
            NewSeller.objects.filter(id=seller_id).delete()
            # Add any other actions upon rejection

        return redirect('Admin:seller_approval')  # Redirect back to the approval page

    context = {
        'pending_registrations': pending_registrations
    }
    return render(request, 'Admin/seller_approval.html', context)

def display_accepted_sellers(request):
    accepted_sellers = NewSeller.objects.filter(vstatus=1)  # Fetch accepted sellers

    if request.method == "POST":
        seller_id = request.POST.get('seller_id')
        action = request.POST.get('action')  # 'reject'

        if action == 'reject':
            NewSeller.objects.filter(id=seller_id).update(vstatus=0)
            # Add any other actions upon rejecting an accepted seller

        return redirect('Admin:display_accepted_sellers')  # Redirect back to the accepted sellers page

    context = {
        'accepted_sellers': accepted_sellers
    }
    return render(request, "Admin/accepted_sellers.html", context)

def display_most_sold_books(request):
    book_data = list(Cart.objects.values('Bookbooking__book_name').annotate(sold_count=Count('id')).order_by('-sold_count')[:10])

    context = {
        'book_data': json.dumps(book_data),
    }

    return render(request, 'Admin/Statistics.html', context)