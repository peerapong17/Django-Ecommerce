from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ('name',)
        # verbose_name = 'หมวดหมู่สินค้า'
        # verbose_name_plural = "ข้อมูลประเภทสินค้า"

    def get_product_by_category(self):
        return reverse('get_product_by_category', args=[self.slug])

    def update_category(self):
        return reverse('update_category', args=[self.id])

    def delete_category(self):
        return reverse('delete_category', args=[self.id])

class Promotion(models.Model):
    name = models.CharField(max_length=255, unique=True)
    class Meta:
        db_table = 'promotion'
        ordering = ('id',)

    def __str__(self):
        return str(self.name)

    def get_product_by_promotion(self):
        return reverse('get_product_by_promotion', args=[self.name])
    
    def update_promotion(self):
        return reverse('update_promotion', args=[self.id])

    def delete_promotion(self):
        return reverse('delete_promotion', args=[self.id])


class OrderStatus(models.Model):
    status = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "orderstatus"

    def __str__(self):
        return self.status

    def get_order_sorted_by_status(self):
        return reverse('getOrderSortedByStatus', args=[self.id])


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)
    promotion = models.ManyToManyField(Promotion, null=True, blank=True)
    image = models.ImageField(upload_to="product", blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        ordering = ('name',)

    def get_detail(self):
        return reverse('productDetail', args=[self.id])


class Cart(models.Model):
    cart_id = models.CharField(max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    class Meta:
        db_table = 'cart'
        ordering = ('date_added',)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name


class Order(models.Model):
    status = models.ForeignKey(
        OrderStatus, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    token = models.CharField(max_length=255, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'
        ordering = ('id',)

    def __str__(self):
        return str(self.id)




class OrderItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orderItem'
        ordering = ('order',)

    def sub_total(self):
        return self.quantity*self.product.price

    def __str__(self):
        return self.product
