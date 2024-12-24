from django.http import HttpResponse
from django.shortcuts import redirect ,render
from shop.models import Product
from .models import Cart
from django.contrib.auth.models import User


def add_to_cart(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        print(pid)
        username = User.objects.get(username = request.session.get('Username'))
        name = Product.objects.get(id=pid)
        print(name)
        product = Cart.objects.filter(product_name = name,username__username = username)
        print(product)
        if product:
            for i in product:
                quantity = i.quantity + 1
                total_price = i.product_price * quantity
                print(quantity)
            Cart.objects.filter(product_name = name,username__username = username).update(quantity = quantity,total_price = total_price)
        

        else:
            product = Product.objects.filter(id= pid)
            for p in product:
                price = p.product_price
                desc = p.product_desc
                image = p.product_image
                total_price=p.product_price
            mycart = Cart.objects.create(username = username,product_name=name,product_price=price,product_desc=desc,product_image=image,total_price=total_price)
            mycart.save()
        return redirect('shop')


def showcart(request):
    username = request.session.get('Username')
    context = {}
    products = Cart.objects.filter(username__username = username)
    print(products)
    context['products'] = products
    return render(request,'cart/cart.html',context)

def deletefromcart(request):
    username = request.session.get('Username')
    if request.method == 'POST':
        pname = request.POST.get('pname')
        print(pname)
        product = Product.objects.get(product_name = pname)
        print(product)
        products = Cart.objects.filter(product_name__product_name = product,username__username = username)
        print('Deleted')
        print(products)

        products.delete()
    return redirect ('showcart')


