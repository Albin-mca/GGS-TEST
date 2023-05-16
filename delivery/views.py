from hashlib import sha256
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import Account, DeliveryBoy, tbl_DeliveryBoy
from orders.models import Order


# Create your views here.
def d_register(request):
    return render(request, 'delivery/d_register.html')


def d_boy_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        vehicle_no = request.POST['vehicle_no']
        license_no = request.POST['license_no']
        password = request.POST['password']
        pswd = sha256(password.encode()).hexdigest()

        delivery_boy = DeliveryBoy(name=name, email=email, phone_number=phone_number, address=address,
                                   vehicle_no=vehicle_no, license_no=license_no, password=pswd)
        delivery_boy.save()

        messages.success(request, 'Registration successfulll')
        return redirect('d_login')

    return render(request, 'accounts/login.html')


@login_required
def delivery_home(request):
    # Add your logic here for the delivery boy home page
    return render(request, 'delivery/delivery_home.html')


from django.shortcuts import render, redirect
from django.contrib import messages, auth


class Accounts:
    pass


def d_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        pswd = sha256(password.encode()).hexdigest()
        delivery_boy = DeliveryBoy.objects.filter(email=email, password=pswd, is_active=1)
        if delivery_boy:
            request.session['email'] = email
            messages.error(request, 'Login success')
            return redirect(delivery_home)
        else:
            messages.error(request, 'Invalid login credentials3')
            return redirect('d_login')

    return render(request, 'delivery/d_login.html')


# def delivery_home(request):
#     if 'email' in request.session:
#         user=request.session['email']
#         data={
#             'user':user
#         }
#         return render(request, 'delivery/delivery_home.html',data)
#     else:
#         return redirect(d_login)


def delivery_home(request):
    # Get the relevant order data from the Order model
    order = Order.objects.all()  # Adjust the query to retrieve the desired order

    if 'email' in request.session:
        user = request.session['email']

        context = {'user': user, 'order': order, }

    return render(request, 'delivery/delivery_home1.html', context)


# change delivery status
def change_status(request, id):
    if 'email' in request.session:
        order = Order.objects.get(id=id)
        order.status = 'Confirmed'
        order.save()
        return redirect(delivery_home)
    else:
        return redirect(d_login)


# change delivered status
def deliverd_status(request, id):
    if 'email' in request.session:
        order = Order.objects.get(id=id)
        order.status = 'Delivered'
        order.save()
        return redirect(delivery_home)
    else:
        return redirect(d_login)


def d_logout(request):
    # Clear the session data
    if 'email' in request.session:
        del request.session['email']

    # Optionally, you can perform additional logout actions

    messages.success(request, 'Logout successful')
    return redirect('d_login')
