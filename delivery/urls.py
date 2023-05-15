from django.urls import path
from . import views

urlpatterns = [
    path('assign_delivery/', views.assign_delivery, name='assign_delivery'),
    path('update_delivery_status/<int:delivery_id>/', views.update_delivery_status, name='update_delivery_status'),

    path('deliveryboy_register/', views.deliveryboy_register, name='deliveryboy_register'),
]
