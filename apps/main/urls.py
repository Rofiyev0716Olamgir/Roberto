from django.urls import path
from .views import HomePageView, ContactView, AboutView

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about')
]