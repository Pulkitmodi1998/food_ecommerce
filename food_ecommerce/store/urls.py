from django.urls import path, include
from .views import signup, profile, index, product_detail, about, view_cart, update_cart, add_to_cart, remove_from_cart
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart/', view_cart, name='cart'),
    path('about/', about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name='store/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('contact/', views.contact, name='contact'), 
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:item_id>/<str:action>/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]
