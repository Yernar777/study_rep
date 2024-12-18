from django.urls import path
from .import views

urlpatterns = [
    path('',views.study,name='home'),
    path('forms/',views.review_functional,name='reviews_form'),
    path('succes/',views.secces,name='succes'),
    path('auth/',views.login_view,name='auth'),
    path('cart/', views.cart_detail, name='cart_detail')

]