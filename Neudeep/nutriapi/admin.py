from django.contrib import admin
from .models import order
from .models import sales

# Register your models here.
@admin.register(order)
class orderadmin(admin.ModelAdmin):
    list_display = ['id','date','brand','product_name','flavour','weight','no_of_cartoons','price_per_cartoon','Distributor_name','area_name','inventory_with','sold_to_type','Product_mrp','upc_bar_code','bar_count']

@admin.register(sales)
class salesadmin(admin.ModelAdmin):
    list_display = ['id','date','brand','product_name','flavour','weight','no_of_cartoons','price_per_cartoon','Distributor_name','area_name','sales_person','total_buisness','inventory_with','sold_to_type','Product_mrp','upc_bar_code','bar_count','ware_house_name','sold_to_id']