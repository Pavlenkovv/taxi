from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('orders/', order_list),
    path('orders/details', order_details),
    path('details', user_order_details),
]
