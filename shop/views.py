from django.shortcuts import get_object_or_404, render

from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(req):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(req,'shop/home.html',context)

@login_required
def search(req): 
    context = {}
    if req.method == 'POST':
        productname = req.POST['productname']
        # print(productname)
        product = Product.objects.filter(product_name__contains = productname)
        print(product)
        context = {'products': product}
    return render(req,'shop/home.html',context)

def details(req):
    if req.method == 'POST':
        id = req.POST.get('pid')
        pro = get_object_or_404(Product, id =id)
        context = {'pro' : pro} 
        return render(req,'shop/details.html',context)
    return render(req,'shop/details.html',context)


def about(request):
    return render(request,'shop/about.html')

