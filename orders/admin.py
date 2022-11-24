from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['order','payment','user','product','quantity','product_price','ordered','created_at']
    list_filter = ['user','ordered','created_at']

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct, OrderProductAdmin)