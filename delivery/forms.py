from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Delivery, DeliveryBoy

class AssignDeliveryForm(forms.Form):
    delivery_id = forms.IntegerField()
    delivery_boy_id = forms.ModelChoiceField(queryset=DeliveryBoy.objects.all())


class DeliveryBoyForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = DeliveryBoy
        fields = ['username', 'email', 'phone_number']