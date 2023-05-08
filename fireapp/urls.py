from django.urls import path
from . import views

urlpatterns = [
    path('fire_index/', views.fire_index, name='fire_index'),

]
