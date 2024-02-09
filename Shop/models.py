from django.db import models

# Create your models here.

class Authors(models.Model):
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True) # valid input: http\https://www.name.domain
    
    def __str__(self) -> str:
        return f'{self.Fname} {self.Lname}'

class Employees(models.Model): # in view, set the permission class to IsAdminUser
    Fname = models.CharField(max_length=200)
    Lname = models.CharField(max_length=200)
    birth_date = models.DateField()
    salary = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.Fname} {self.Lname}'

class Books(models.Model): # in view, set the permission class to IsAthenticated
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING)
    genre = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    price = models.CharField(max_length=300)
    publishing_yaer = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title


class Buyers(models.Model): # in view, set the permission class to IsAthenticated
    buyer_fname = models.CharField(max_length=200)
    buyer_lname = models.CharField(max_length=200)
    bought_book = models.ForeignKey(Books, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.buyer_fname} {self.buyer_lname}'
    

# We have to impelement a login page -- DONE
# Only admins can see the data, so it means:
# u go to the Authors url, u see a login page, if u r an admin, u enter ur user pass and then u can see the data
# if u r not an admin and u r doesnt have an account, then u r not supposed to see anything. -- DONE

# The other thing is about employees, does all the employees should have an account?
# or only the ones that the boss is verified?
# and even more, do we have an known boss account on the top? 