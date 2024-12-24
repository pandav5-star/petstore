from django.http import HttpResponse
from django.shortcuts import render,redirect
from cart.models import Cart
from django.contrib.auth.models import User
import random
import string
from .models import Order,Order_item
import datetime

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def checkout(request):
    username = request.session.get('Username')
    context = {}
    total_amount = 0 
    products = Cart.objects.filter(username__username = username)
    for i in products:
        total_amount += i.product_price
    context['products'] = products
    context['total_amount'] = total_amount
    print(total_amount)
    
    return render(request,'checkout/checkout.html',context)


def order(request):
    if request.method == 'POST':
       username = User.objects.get(username = request.session.get('Username'))
       first= request.POST.get('first')
       last = request.POST.get('last')
       email = request.POST.get('email')
       city = request.POST.get('city') + request.POST.get('zipco')
       full_name = first + last

       # to generate random order id

    upper = string.ascii_uppercase
    num = string.digits
    all = upper + num
    temp = random.sample(all,10)
    order_id = "ORD" + "".join(temp)
    print(order_id)
    order_details = Order.objects.create(order_id = order_id,username = username,full_name = full_name,email = email ,shipping_address = city,date_ordered = datetime)
    order_details.save()

    paypal_transaction_id = request.POST.get("paypal-button-id")
    print(paypal_transaction_id)
        
     
     #check if the payment was amde with paypal

    if paypal_transaction_id:
        order_id = Order.objects.get(username__username = username,placed=False)
        cart_item = Cart.objects.filter(username__username = username)
        for cart in cart_item:
            Order_item.objects.create(
                order = order_id,
                product = cart.product_name,
                username = username,
                quantity = cart.quantity,
                price = cart.product_price,

            )
            cart.delete()
        Order.objects.filter(username__username = username,placed = False).update(placed = True)
        return redirect('success')
    
    #handle the case where paypal id is not provided
    
    else:
        return HttpResponse("Invalid payment information")
    
    #return render(request,'checkout/order.html')

def success(request):
    context = {}
    username = request.session.get('Username')
    order_details = Order.objects.get(username__username = username,email_sent = False)
    subject = 'Order Confirmation '+str(order_details.order_id)
    message = 'Dear '+str(order_details.username)+'\n'+'Thank you for your order'
    address = order_details.username.email
    print(address)
    try:
        send_mail(subject,message,settings.EMAIL_HOST_USER,[address])
        context['result'] = 'Email sent successfully'
        Order.objects.filter(username__username = username,email_sent = False).update(email_sent = True)
    except Exception as e:
        context['result'] = f'Erroe sending email: {e}'

    return render(request,'checkout/success.html')


