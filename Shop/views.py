from rest_framework import generics, permissions, viewsets

from .models import Authors, Employees, Books,  Buyers
from .serializers import AuthorsSerializer, EmployeesSerializer, BooksSerializer, BuyersSerializer

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [permissions.IsAdminUser]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [permissions.IsAuthenticated]

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from rest_framework.parsers import JSONParser
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# class AuthorList(generics.ListCreateAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorsSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorsSerializer
#     # permission_classes = [permissions.IsAuthenticated]
    
# -------------------------------------------------------------------------------------- #    

# class AuthorList(APIView):
#     def get(self, request, format=None):
#         authors = Authors.objects.all()
#         serializer = AuthorsSerializer(authors, many=True)
            
#         return Response(serializer.data)
        
#     def post(self, request, format=None):
#         serializer = AuthorsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class AuthorDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Authors.objects.get(pk=pk)
#         except Authors.DoesNotExist:    
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, pk, format=None):
#         author = self.get_object(pk)
#         serializer = AuthorsSerializer(author)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         authors = self.get_object(pk)
#         serializer = AuthorsSerializer(authors, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED) # should this have status?
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         authors = self.get_object(pk)
#         authors.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------- #

# @api_view(['GET', 'POST'])
# # @csrf_exempt
# def author_list(request):
#     if request.method == 'GET':
#         authors = Authors.objects.all()
#         serializer = AuthorsSerializer(authors, many=True)
        
#         return Response(serializer.data)#, safe=False)
        

#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = AuthorsSerializer(Authors, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)#, safe=False)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# # @csrf_exempt
# def author_detail(request, pk):
#     try:
#         authors = Authors.objects.get(pk=pk)
#     except Authors.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AuthorsSerializer(authors)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = AuthorsSerializer(authors, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#     elif request.method == 'DELETE':
#         authors.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
