from django.shortcuts import render, get_object_or_404, redirect
from store.models import Category, Product, Cart, CartItem, Order, OrderItem, Promotion
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe


def index(request, category_slug=None, promotion=None):
    products = None
    category = None
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=category, available=True).all()
    elif promotion is not None:
        promotion = get_object_or_404(Promotion, name=promotion)
        products = Product.objects.filter(
            promotion=promotion, available=True).all()
    else:
        products = Product.objects.all().filter(available=True)

    # 12 / 3 = 4
    paginator = Paginator(products, 3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        productperPage = paginator.page(page)
    except (EmptyPage, InvalidPage):
        productperPage = paginator.page(paginator.num_pages)

    return render(request, 'store/index.html', {'products': productperPage, 'promotion': promotion})


def product_detail(request, product_id):
    try:
        # product = Product.objects.get(
        #     category__slug=category_slug, slug=product_slug)
        product = Product.objects.get(id=product_id)
    except Exception as e:
        raise e
    return render(request, 'store/product.html', {'product': product})


# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart


@login_required(login_url='sign_in_user')
def add_to_cart(request, product_id):
    # ดึงสินค้าที่เราซื้อมาใช้งาน
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        qty = int(request.POST['qty'])
        try:
            cart = Cart.objects.get(cart_id=request.user.id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=request.user.id)
            cart.save()

        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            if cart_item.quantity < cart_item.product.stock:
                cart_item.quantity += qty

        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=qty
            )
        cart_item.save()


def cart_detail(request):
    total = 0
    cart_items = None
    cart=None
    try:
        cart = Cart.objects.get(cart_id=request.user.id)  # ดึงตะกร้า
        cart_items = cart.cartitem_set.all()
        # cart_items=CartItem.objects.filter(cart=cart,active=True) #ดึงข้อมูลสินค้าในตะกร้า
        for item in cart_items:
            total += (item.product.price * item.quantity)
    except Exception as e:
        pass

    stripe.api_key = settings.SECRET_KEY
    stripe_total = int(total * 100)
    description = "Payment Online"
    data_key = settings.PUBLIC_KEY

    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            name = request.POST['stripeBillingName']
            address = request.POST['stripeBillingAddressLine1']
            city = request.POST['stripeBillingAddressCity']
            postcode = request.POST['stripeShippingAddressZip']
            customer = stripe.Customer.create(
                email=email,
                source=token
            )

            print(customer)

            stripe.Charge.create(
                amount=stripe_total,
                currency='thb',
                description=description,
                customer=customer.id
            )
            # บันทึกข้อมูลใบสั่งซื้อ
            order = Order.objects.create(
                user_id=request.user.id,
                status_id=1,
                name=name,
                address=address,
                city=city,
                postcode=postcode,
                total=total,
                email=email,
                token=token
            )

            order.save()

            # บันทึกรายการสั่งซื้อ
            for item in cart_items:
                order_item = OrderItem.objects.create(
                    product=item.product,
                    quantity=item.quantity,
                    order_id=order.id
                )

                order_item.save()
                # ลดจำนวน Stock
                product = Product.objects.get(id=item.product.id)
                product.stock = int(product.stock - item.quantity)
                product.save()

            cart.delete()

            return redirect('thank_you')

        except stripe.error.CardError as e:
            return False, e

    return render(request, 'cart/cart_detail.html',
                  dict(cart_items=cart_items, total=total,
                       data_key=data_key,
                       stripe_total=stripe_total,
                       description=description
                       ))


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=request.user.id)
    cart_items = cart.cartitem_set.all()
    for item in cart_items:
        if item.product.id == product_id:
            item.delete()

    # another way
    # product = get_object_or_404(Product, id=product_id)
    # cartItem = CartItem.objects.get(product=product, cart=cart)
    # cartItem.delete()

    return redirect('cartDetail')


def search(request):
    products = Product.objects.filter(name__contains=request.POST['search'])
    return render(request, 'store/index.html', {'products': products})


def order_history(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user.id)
        return render(request, 'cart/orders.html', {'orders': orders})
    return redirect("signInUser")


def order_detail(request, order_id):
    if request.user.is_authenticated:
        order = Order.objects.get(user_id=request.user.id, id=order_id)
        order_items = order.orderitem_set.all()
        # orderitem=OrderItem.objects.filter(order=order)
        return render(request, 'cart/order_detail.html', {'order': order, 'order_items': order_items})
    return redirect("signInUser")


def thank_you(request):
    return render(request, 'store/thank_you.html')
