from django.shortcuts import get_object_or_404, redirect, render
from django.core.files.storage import FileSystemStorage

from store.models import Product, Category, Promotion
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'product/index.html')


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        slug = request.POST['slug']
        desc = request.POST['desc']
        price = request.POST['price']
        image = request.FILES['image']
        stock = request.POST['stock']
        categories = request.POST.getlist('categories')
        promotions = request.POST.getlist('promotions')
        available = request.POST.getlist('available')

        product = Product.objects.create(name=name, slug=slug, description=desc, price=price, image=image, stock=stock,
                                         available=available[0])

        for category in categories:
            product.category.add(category)

        for promotion in promotions:
            product.promotion.add(promotion)

        product.save()
        messages.success(request, "Create product success")
        return redirect('products')

    return render(request, 'product/create.html')


def update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        name = request.POST['name']
        slug = request.POST['slug']
        desc = request.POST['desc']
        price = request.POST['price']
        stock = request.POST['stock']
        selected_categories = [int(category) for category in request.POST.getlist('categories')]
        selected_promotions = [int(promotion) for promotion in request.POST.getlist('promotions')]
        product_categories = [category.id for category in product.category.all()]
        product_promotions = [promotion.id for promotion in product.promotion.all()]

        product.name = name
        product.slug = slug
        product.description = desc
        product.price = price
        product.stock = stock

        if request.POST.getlist('available'):
            product.available = True
        else:
            product.available = False

        for selected_category in selected_categories:
            if selected_category in product_categories:
                for product_category in product_categories:
                    if product_category not in selected_categories:
                        category = Category.objects.get(id=product_category)
                        category.product_set.remove(product.id)
            else:
                category = Category.objects.get(id=selected_category)
                category.product_set.add(product.id)
                for product_category in product_categories:
                    if product_category not in selected_categories:
                        category = Category.objects.get(id=product_category)
                        category.product_set.remove(product.id)

        for selected_promotion in selected_promotions:
            if selected_promotion in product_promotions:
                for product_promotion in product_promotions:
                    if product_promotion not in selected_promotions:
                        promotion = Promotion.objects.get(id=product_promotion)
                        promotion.product_set.remove(product.id)
            else:
                promotion = Promotion.objects.get(id=selected_promotion)
                promotion.product_set.add(product.id)
                for product_promotion in product_promotions:
                    if product_promotion not in selected_promotions:
                        promotion = Promotion.objects.get(id=product_promotion)
                        promotion.product_set.remove(product.id)

        if request.FILES and request.FILES["image"]:
            if str(request.FILES["image"].content_type).startswith("image"):
                fs = FileSystemStorage()
                fs.delete(str(product.image))
                product.image = request.FILES["image"]
            else:
                messages.warning(
                    request, "Invalid image type, please type again")
                return render(request, 'product/update.html', {"product": product})

        product.save()
        messages.success(request, "Update product success")

        return redirect('products')

    return render(request, 'product/update.html', {"product": product})


def delete(request, product_id):
    fs = FileSystemStorage()
    product = get_object_or_404(Product, id=product_id)
    fs.delete(str(product.image))
    product.delete()
    messages.success(request, "Delete product success")
    return redirect("products")
