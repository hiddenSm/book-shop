from django.urls import path, include
from .views import author_list, author_detail

urlpatterns = [
    path('authors/', author_list, name='authorList'),
    path('authors/<int:pk>', author_detail, name='authorDetail'),
    
]