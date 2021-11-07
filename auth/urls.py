
from auth import views
from django.urls import path

urlpatterns = [
    path('create', views.sign_up_user, name="signUpUser"),
    path('login', views.sign_in_user, name="signInUser"),
    path('logout', views.sign_out_user, name="signOutUser"),
]

