from store.models import Category, Cart, OrderStatus, Product, Promotion


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_orderStatus(request):
    orderStatus = OrderStatus.objects.all()
    return dict(orderStatus=orderStatus)


def get_promotions(request):
    promotions = Promotion.objects.all()
    return dict(promotions=promotions)


def get_products(request):
    products = Product.objects.all()
    return dict(products=products)


def counter(request):
    item_count = 0
    print(request.path)
    if 'admin_management' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=request.user.id)
            # cart_Item=CartItem.objects.all().filter(cart=cart[:1])
            item_count = cart.cartitem_set.all().count()
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
