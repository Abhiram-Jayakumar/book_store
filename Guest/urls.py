from django.urls import path
from Guest import views

app_name = 'Guest'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('userregister/', views.register, name="register"),
    path('sellerregister/', views.sellerregister, name="sellerregister"),
    path('index/', views.index, name="index"),
    path('Tnx/', views.Thankyou, name="thankyou"),
    path('ebook_list/', views.ebook_list, name="ebook_list"),
    path('Product/<int:book_id>/', views.Productd, name="Productd"),
    path('Ebookdisp/<int:bbook_id>/', views.Ebookdisp, name="Ebookdisp"),
    path('seller-info/<int:book_id>/', views.book_seller_info, name='book_seller_info'),
    path('ViewReview/<int:book_id>/', views.displayreviews, name='Guest_book_reviews'),
    path('EGuestauthor-detail/<int:ebook_id>/', views.Guest_author_detail_view, name='Guestauthor_detail'),
    path('ebook/<int:ebook_id>/reviews/', views.Guest_view_ebook_reviews, name='Guest_view_ebook_reviews'),


]
