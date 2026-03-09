from django.urls import path
from .views import login_view, logout_view, register_choice, register_shopper, register_merchant

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('register/', register_choice, name='register_choice'),
    path('register/shopper/', register_shopper, name='register_shopper'),
    path('register/merchant/', register_merchant, name='register_merchant'),
]