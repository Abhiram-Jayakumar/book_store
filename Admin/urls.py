from django.urls import path
from Admin import views

app_name = 'Admin'

urlpatterns = [
path('AdminHome/', views.AdminHome, name="AdminHome"),
path('View_complaints/', views.view_complaints, name="Viewcomplaints"),
path('bookingdetails/', views.view_booking_details, name="bookingdetails"),
path('seller-approval/', views.seller_approval, name='seller_approval'),
path('accepted-sellers/', views.display_accepted_sellers, name='display_accepted_sellers'),
path('most-sold-books/', views.display_most_sold_books, name='most_sold_books'),

]
