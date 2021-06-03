from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .serializers import BookSerializer
from Books.models import Book as bk
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication\

from rest_framework.permissions import IsAuthenticated
# api/books creating and listing books
# Create your views here.

class BooksList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        book = bk.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#api/books/id
# two authentication sesion based(username, password validation), token based authentication(when user login a token is
# assigned based on that)
# when using token based auth logout from only particular devices
class BookDetails(APIView):
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )

    def get_object(self,pk):
        try:
            return bk.objects.get(id=pk)
        except:
            raise Http404
    def get(self,request,pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        book=self.get_object(pk)
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status = status.HTTP_202_ACCEPTED)








