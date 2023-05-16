from django.urls import path
from . import views

# app_name = 'delivery'

urlpatterns = [path('d_register/', views.d_register, name='d_register'),
    path('d_boy_register/', views.d_boy_register, name='d_boy_register'),
    path('delivery_home/', views.delivery_home, name='delivery_home'), path('d_login/', views.d_login, name='d_login'),
    path('delivery_home/', views.delivery_home, name='delivery_home'),
    path('change_status/<int:id>/', views.change_status, name='change_status'),
    path('deliverd_status/<int:id>/', views.deliverd_status, name='deliverd_status'),
    path('d_logout/', views.d_logout, name='d_logout'),

    # Add more URL patterns for other delivery views
]
