
from auth import views
from django.urls import path

urlpatterns = [
    path('create',views.signUpUser,name="signUpUser"),
    path('login',views.signInUser,name="signInUser"),
    path('logout',views.signOutUser,name="signOutUser"),
]

