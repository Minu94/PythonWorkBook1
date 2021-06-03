from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import BooksList, BookDetails


urlpatterns = [path('books',BooksList.as_view()),
               path('books/<int:pk>',BookDetails.as_view()),

]