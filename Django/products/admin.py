from django.contrib import admin
from .models import products,offer
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock']
class OfferAdmin(admin.ModelAdmin):
    list_display=['code','description','discount']
admin.site.register(products,ProductAdmin)
admin.site.register(offer,OfferAdmin)
# Register your models here.
