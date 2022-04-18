from nutriapi import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('orderapi/',views.order_api),
    path('salesapi/',views.sales_api),
    path('orderpostapi',views.orderpostapi),
]
