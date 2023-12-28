from django.urls import path
from BookAuthor import views

app_name = 'BookAuthor'

urlpatterns = [

path('authorhome/', views.authorhome, name="authorhome"),
path('addbook/',views.addbook,name="addbook"), 
path('authorprofile/',views.Authorprofile,name="authprofile"), 
path('AddEbook/',views.AddEbook,name="AddEbook"), 
path('seller-bookings/', views.seller_view_bookings, name='seller_bookings'),
path('seller-added-books/', views.seller_added_books, name='seller_added_books'),
path('update_seller_profile/<int:cid>/', views.update_seller_profile, name='update_seller_profile'),
path('Sellerupdate_password/<int:cid>/', views.Seller_update_password, name='seller_update_password'),


]
