from django.urls import path
from User import views

app_name = 'User'

urlpatterns = [
        path('userhome/', views.homeuser, name="userhome"),
        path('tnxshop/', views.tnxshop, name="tnxshop"),
        path('Cart/<int:cid>/', views.cart_view, name='cart'),
        path('updateuser/<int:cid>/',views.updateuser,name="Updateuser"),
        path('ViewProfile/',views.userdetails,name="View-userProfile"),
        path('payment/<int:pid>',views.payment,name="payment"),
        path('bookingdetailsofuser/', views.view_booking, name="bookingdetailsUser"),
        path('Productdetail/<int:book_id>/', views.Productdetail, name="Product"),
        path('ebooklistUser/', views.ebooklistUser, name="ebooklistUser"),
        path('EbookUserdisp/<int:bbook_id>/', views.EbookdispUser, name="Ebookdispuser"),
        path('seller-infoUser/<int:book_id>/', views.book_sellerinfo, name='book_sellerinfo'),
        path('Add-review/<int:book_id>/', views.review, name='Addreview'),
        path('ViewReview/<int:book_id>/', views.display_reviews, name='book_reviews'),
        path('Complaint/', views.complaint, name="Complaint"),
        path('ECart/<int:bbook_id>/', views.Ecart_view, name='Ecart'), 
        path('Epayment/<int:pid>/', views.Epayment, name="Epayment"),
        path('payment/success/<int:pid>/', views.payment_success, name='payment_success'),
        path('download/<int:pid>/', views.download_ebook, name='download_ebook'),
        path('author-detail/<int:ebook_id>/', views.author_detail_view, name='author_detail'),
        path('update_profile/<int:cid>/', views.update_profile, name='update_profile'),
        path('update_password/<int:cid>/', views.update_password, name='update_password'),
        path('User/Track/<int:booking_id>/', views.track_order, name='track'),
        path('order-details/<int:booking_id>/', views.view_order_details, name='order_details'),
        path('add-ebook-review/<int:ebook_id>/', views.add_ebook_review, name='add_ebook_review'),
        path('ebook/<int:ebook_id>/reviews/', views.view_ebook_reviews, name='view_ebook_reviews'),
]