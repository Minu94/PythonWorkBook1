from django.urls import path,include
from . import views

urlpatterns = [
    path('addproduct', views.AddProduct.as_view(), name="addproduct"),
    path('listproduct', views.ListProduct.as_view(), name='listproduct'),
    path('editproduct/<int:pk>', views.EditProduct.as_view(), name='editproduct'),
    path('deleteproduct/<int:pk>', views.DeleteProduct.as_view(), name='deleteproduct'),
    path('addpurchase', views.AddPurchase.as_view(), name="addpurchase"),
    path('listpurchase', views.ListPurchase.as_view(), name='listpurchase'),
    path('editpurchase/<int:pk>', views.EditPurchase.as_view(), name='editpurchase'),
    path('deletepurchase/<int:pk>', views.DeletePurchase.as_view(), name='deletepurchase'),
    path('order', views.OrderView.as_view(), name="order"),
    path('orderlines/<int:billno>', views.OrderLineView.as_view(), name='orderlines'),
]
