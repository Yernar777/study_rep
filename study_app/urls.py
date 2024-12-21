from django.urls import path
from .import views

urlpatterns = [
    path('',views.study,name='home'),
    path('forms/',views.review_functional,name='reviews_form'),
    path('succes/',views.secces,name='succes'),
    path('auth/',views.login_view,name='auth'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views,checkout, name='checkout'),
]