from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from store.models import Category, Order, OrderStatus, Promotion

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


def category(request, category_id=None):
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        category.delete()
        messages.success(request, "Category deleted successfully")
        return redirect('categories')

    return render(request, 'category/index.html')


def createCategory(request):
    if request.method == "POST":
        name = request.POST['name']
        slug = request.POST['slug']
        if not name:
            messages.warning(request, "name can not be blank")

        elif not slug:
            messages.warning(request, "slug can not be blank")

        else:
            category = Category.objects.create(name=name, slug=slug)
            category.save()
            messages.success(request, "Create category success")
            return redirect('categories')

    return render(request, 'category/create.html')


def updateCategory(request, category_id):
    # category = Category.objects.get(id=category_id)

    # another way
    category = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        name = request.POST['name']
        slug = request.POST['slug']
        if not name:
            messages.warning(request, "name can not be blank")

        elif not slug:
            messages.warning(request, "slug can not be blank")

        else:
            category.name = name
            category.slug = slug
            category.save()
            messages.success(request, "Update category success")
            return redirect('categories')

    return render(request, 'category/update.html', {"category": category})


def promotion(request, promotion_id=None):
    if promotion_id is not None:
        promotion = Promotion.objects.get(id=promotion_id)
        promotion.delete()
        messages.success(request, "Promotion deleted successfully")
        return redirect('promotions')

    return render(request, 'promotion/index.html')


def createPromotion(request):
    if request.method == "POST":
        name = request.POST['name']
        if not name:
            messages.warning(request, "name can not be blank")

        else:
            promotion = Promotion.objects.create(name=name)
            promotion.save()
            messages.success(request, "Create promotion success")
            return redirect('promotions')

    return render(request, 'promotion/create.html')


def updatePromotion(request, promotion_id):
    promotion = get_object_or_404(Promotion, id=promotion_id)

    if request.method == "POST":
        name = request.POST['name']
        if not name:
            messages.warning(request, "name can not be blank")

        else:
            promotion.name = name
            promotion.save()
            messages.success(request, "Update promotion success")
            return redirect('promotions')

    return render(request, 'promotion/update.html', {"promotion": promotion})

