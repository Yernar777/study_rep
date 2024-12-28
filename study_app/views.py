from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from .forms import OrderForm


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_price = sum(item.get_total_price() for item in cart.items.all())
    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

@login_required
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()  
    return redirect('cart_detail')






def review_functional(request):
    form = ReviewForms()
    form1 = ReviewForms1()
    
    if request.method == 'POST':
        form = ReviewForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = ReviewForms()

    if request.method == 'POST':
        form1 = ReviewForms1(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('succes')
    return render(request, 'forms.html',{'form': form, 'form1': form1,})


def secces(request):
    return render(request,'succes.html')





def study(request):
    products = Product.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    context = {'form':form,'products':products,}
    return render(request, 'study.html',context=context)





def login_view(request):
    form = LoginForm(request, data = request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
    context ={'form':form}

    return render(request, 'login.html',context=context)


def logout_view(request):
    logout(request)
    return redirect('login')




def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sum(item.get_total_price() for item in cart.items.all())
            order.save()


            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
            
            cart.items.all().delete()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form, 'cart': cart})

def order_success(request):
    return render(request, 'order_success.html')



def cross(request,id):
    products = Product2.objects.filter(category_id=id)
    return render(request,'cross_products.html',{'products':products})

