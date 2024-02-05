from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser

from .models import Authors#, Books, Employees, Buyers
from .serializers import AuthorsSerializer

# Create your views here.

@api_view(['GET', 'POST'])
# @csrf_exempt
def author_list(request):
    if request.method == 'GET':
        authors = Authors.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        
        return Response(serializer.data)#, safe=False)
        

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = AuthorsSerializer(Authors, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
def author_detail(request, pk):
    try:
        authors = Authors.objects.get(pk=pk)
    except Authors.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorsSerializer(authors)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = AuthorsSerializer(authors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'DELETE':
        authors.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)