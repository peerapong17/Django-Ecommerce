
from dashboard import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('confirm/order/<int:bill_id>', views.confirmOrder, name="confirmOrder"),
    path('cancel/order/<int:bill_id>', views.cancelOrder, name="cancelOrder"),
    path('get/order/<int:status_id>', views.dashboard,
         name="getOrderSortedByStatus"),
    path('categories', views.category, name="categories"),
    path('categories/create', views.createCategory, name="create_category"),
    path('categories/update/<int:category_id>', views.updateCategory, name="update_category"),
    path('categories/delete/<int:category_id>',
         views.category, name="delete_category"),
    path('promotions', views.promotion, name="promotions"),
    path('promotions/create', views.createPromotion, name="create_promotion"),
    path('promotions/update/<int:promotion_id>', views.updatePromotion, name="update_promotion"),
    path('promotions/delete/<int:promotion_id>',
         views.promotion, name="delete_promotion"),
]
