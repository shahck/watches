from django.shortcuts import redirect, render
from cart.models import CartItem
from orders.models import Order
# from store.models import Product
# from .models import OrderProduct, Payment
from .forms import OrderForm
import datetime

# from django.contrib.auth.decorators import login_required
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage

# import razorpay
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest
# from prjct import settings

# Create your views here.


def place_order(request, quantity=0, total=0):
    current_user = request.user


    cart_items =CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count < 0:
        return redirect('store')

    grand_total = 0
    tax  = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2 * total)/100
    grand_total = total + tax

    
    if request.method == 'POST':
        form = OrderForm(request.POST)

        # print(form)
        
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.order_note = form.cleaned_data['order_note']
            data.pincode = form.cleaned_data['pincode']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate Order number
            year = int(datetime.date.today().strftime('%Y'))
            month = int(datetime.date.today().strftime('%m'))
            date = int(datetime.date.today().strftime('%d'))
            d = datetime.date(year, month, date)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            
            # request.session['order_number'] = order_number
            # print(f"order no : ${request.session['order_number']}")
            # return redirect('payment')
    
        else:
            return redirect('checkout')