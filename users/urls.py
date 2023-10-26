from django.urls import path
from .views import register, profile
from  django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
]