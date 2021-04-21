from django.contrib import admin
from django.urls import include, path

from main.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/', order_list),
    path('orders/details', order_details),
]
