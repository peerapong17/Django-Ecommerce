from store import views
from django.urls import path

    

urlpatterns = [
    path('',views.index,name="home"),
    path('category/<slug:category_slug>',views.index,name="get_product_by_category"),
    path('product/<slug:category_slug>/<slug:product_slug>',views.productDetail,name='productDetail'),
    path('cart/add/<int:product_id>',views.addToCart,name="addToCart"),
    path('cartdetail/',views.cartDetail,name="cartDetail"),
    path('cart/remove/<int:product_id>',views.removeFromCart,name="removeFromCart"),
    path('search/',views.search,name='search'),
    path('orderHistory/',views.orderHistory,name="orderHistory"),
    path('order/<int:order_id>',views.orderDetail,name="orderDetails"),
    path('cart/thankyou',views.thankyou,name='thankyou')
]

