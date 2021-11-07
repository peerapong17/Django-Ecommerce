from product import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="products"),
    path('product/create', views.create, name="create_product"),
    path('product/update/<int:product_id>', views.update, name="update_product"),
    path('product/delete/<int:product_id>', views.delete, name="delete_product"),
]
