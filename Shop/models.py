from django.db import models

# Create your models here.

class Authors(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.Fname} {self.Lname}'

# class Books(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Authors)
#     genre = models.CharField(max_length=200)
#     publisher = models.CharField(max_length=200)
#     price = models.CharField(max_length=300)
#     publishing_yaer = models.IntegerField()
    
#     def __str__(self) -> str:
#         return self.title


# class Employees(models.Model):
#     Fname = models.CharField(max_length=200)
#     Lname = models.CharField(max_length=200)
#     birth_date = models.DateField()
#     salary = models.CharField(max_length=200)
#     email = models.EmailField(null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.Fname} {self.Lname}'


# class Buyers(models.Model):
#     buyer_fname = models.CharField(max_length=200)
#     buyer_lname = models.CharField(max_length=200)
#     bought_book = models.ForeignKey(Books)

#     def __str__(self) -> str:
#         return f'{self.buyer_fname} {self.buyer_lname}'