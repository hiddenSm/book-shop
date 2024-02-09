from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Authors, Employees, Books, Buyers

# sepehr:1234
# admin1:admin1@sepehr

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['Fname', 'Lname', 'birth_date', 'email', 'website']

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['Fname', 'Lname', 'birth_date', 'salary', 'email']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'author', 'genre', 'publisher', 'price', 'publishing_yaer']

class BuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = ['buyer_fname', 'buyer_lname', 'bought_book']



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']