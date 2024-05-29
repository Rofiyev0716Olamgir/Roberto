from django.urls import path
from .views import ServicesListView, service_detail, LikeRedirectView
app_name = 'services'

urlpatterns = [
    path('services_list/', ServicesListView.as_view(), name='services_list'),
    path('service_detail/<slug:slug>/', service_detail, name='service_detail'),
    path('service_lake/<int:eid>', LikeRedirectView.as_view(), name='comment_lake')
]