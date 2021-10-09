from store.models import Category, Cart, OrderStatus


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_orderStatus(request):
    orderStatus = OrderStatus.objects.all()
    return dict(orderStatus=orderStatus)


def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=request.user.id)
            # cart_Item=CartItem.objects.all().filter(cart=cart[:1])
            cart_Item = cart.cartitem_set.all()
            for item in cart_Item:
                item_count += item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
