from django.urls import path
from django.urls import reverse_lazy
from .views import RegisterView, LoginView, LogoutView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='account/login.html',
        next_page=reverse_lazy('main:home'),
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
