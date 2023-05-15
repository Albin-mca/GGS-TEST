from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Delivery, DeliveryBoy
from .forms import AssignDeliveryForm

def assign_delivery(request):
    if request.method == 'POST':
        form = AssignDeliveryForm(request.POST)
        if form.is_valid():
            delivery_id = form.cleaned_data['delivery_id']
            delivery_boy_id = form.cleaned_data['delivery_boy_id']
            delivery = Delivery.objects.get(id=delivery_id)
            delivery.delivery_boy_id = delivery_boy_id
            delivery.save()
            messages.success(request, 'Delivery assigned successfully')
            return redirect('assign_delivery')
    else:
        form = AssignDeliveryForm()

    return render(request, 'delivery/assign_delivery.html', {'form': form})

def update_delivery_status(request, delivery_id):
    delivery = Delivery.objects.get(id=delivery_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        delivery.status = status
        delivery.save()
        messages.success(request, 'Delivery status updated successfully')
        return redirect('assign_delivery')
    else:
        return render(request, 'delivery/update_delivery_status.html', {'delivery': delivery})


from django.shortcuts import render, redirect
from .forms import DeliveryBoyForm

def deliveryboy_register(request):
    if request.method == 'POST':
        dform = DeliveryBoyForm(request.POST)
        if dform.is_valid():
            dform.save()
            return redirect('deliveryboy_login')
    else:
        dform = DeliveryBoyForm()

    return render(request, 'delivery/dregister.html', {'dform': dform})
