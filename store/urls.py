from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls.static import static
from django.conf import settings

    

urlpatterns = [
    path('admin/', admin.site.urls),
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

# product/fashion/shoes-men
# product/toys/lego

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

