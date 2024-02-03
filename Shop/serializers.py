from rest_framework import serializers
from .models import Authors#, Books, Employees, Buyers

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['Fname', 'Lname', 'birth_date', 'email', 'website']

# class BooksSerializer(serializers.Serializer):
#     class Meta:
#         model = Books
#         fields = ['title', 'author', 'genre', 'publisher', 'price', 'publishing_yaer']

# class EmployeesSerializer(serializers.Serializer):
#     class Meta:
#         model = Employees
#         fields = ['Fname', 'Lname', 'birth_date', 'salary', 'email']

# class BuyersSerializer(serializers.Serializer):
#     class Meta:
#         model = Buyers
#         fields = ['buyer_fname', 'buyer_lname', 'bought_book']