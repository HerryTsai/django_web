from django.urls import path
from .views import index, listing, disp_detail


urlpatterns = [
    path('', index),
    path('list/', listing),
    path('list/<int:id>/', disp_detail),
]