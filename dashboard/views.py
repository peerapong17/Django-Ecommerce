from django.shortcuts import redirect, render
from store.models import Order, OrderStatus

# Create your views here.


def dashboard(request, status_id=None):
    if status_id is not None:
        print(status_id)
        orders = Order.objects.filter(status_id=status_id).all()
    else:
        orders = Order.objects.all()
    return render(request, "dashboard/admin.html", {"orders": orders})


def confirmOrder(request, bill_id):
    order = Order.objects.get(id=bill_id)
    order.status_id = 2
    order.save()
    return redirect('dashboard')


def cancelOrder(request, bill_id):
    order = Order.objects.get(id=bill_id)
    order.status_id = 3
    order.save()
    return redirect('dashboard')
