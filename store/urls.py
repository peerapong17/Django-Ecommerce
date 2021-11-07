from store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('<str:promotion>', views.index, name="get_product_by_promotion"),
    path('category/<slug:category_slug>', views.index, name="get_product_by_category"),
    path('product/<int:product_id>', views.product_detail, name='productDetail'),
    path('cart/add/<int:product_id>', views.add_to_cart, name="addToCart"),
    path('cartdetail/', views.cart_detail, name="cartDetail"),
    path('cart/remove/<int:product_id>', views.remove_from_cart, name="removeFromCart"),
    path('search/', views.search, name='search'),
    path('orderHistory/', views.order_history, name="orderHistory"),
    path('order/<int:order_id>', views.order_detail, name="orderDetails"),
    path('cart/thankyou', views.thank_you, name='thank_you')
]
