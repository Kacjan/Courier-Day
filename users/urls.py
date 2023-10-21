from django.urls import path
from .views import register, profile
from  django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='form.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('profile', profile, name='profile'),
]