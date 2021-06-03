

from django.urls import path
from . import views

urlpatterns = [path('create',views.BookCreate.as_view(),name="create"),
               path('list',views.BookList.as_view(),name="list"),
               path('edit/<int:pk>',views.BookEdit.as_view(),name="edit"),
               path('details/<int:pk>',views.BookView.as_view(),name='details'),
               path('delete/<int:pk>',views.BookDelete.as_view(),name="delete"),
]
