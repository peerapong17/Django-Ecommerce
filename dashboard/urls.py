
from dashboard import views
from django.urls import path

urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('confirm/order/<int:bill_id>',views.confirmOrder,name="confirmOrder"),
    path('cancel/order/<int:bill_id>',views.cancelOrder,name="cancelOrder"),
    path('get/order/<int:status_id>',views.dashboard,name="getOrderSortedByStatus"),
]

