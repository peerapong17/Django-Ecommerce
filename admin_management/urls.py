
from admin_management import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name="admins"),
    path('create', views.create, name="create_admin"),
    path('update/<int:id>', views.update, name="update_admin"),
    path('delete/<int:id>', views.delete, name="delete_admin"),
]

