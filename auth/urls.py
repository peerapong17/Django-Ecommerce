from auth import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create', views.sign_up_user, name="signUpUser"),
    path('login', views.sign_in_user, name="signInUser"),
    path('logout', views.sign_out_user, name="signOutUser"),
    path(
        'password_reset',
        auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"),
        name="reset_password"
    ),
    path(
        'password_reset_done',
        auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"),
        name="password_reset_done"
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        'password_reset_complete',
        auth_views.PasswordResetCompleteView.as_view(template_name="auth/password_reset_complete.html"),
        name="password_reset_complete"
    )
]
